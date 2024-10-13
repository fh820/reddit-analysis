from django.conf import settings
from django.shortcuts import render
import praw
from transformers import pipeline
from urllib.parse import urlparse  # Import urlparse

# Initialize the sentiment analysis pipeline outside of the view function for efficiency
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def home(request):
    posts = []
    url = None  # Initialize the URL
    overall_sentiment = None

    if request.method == 'POST':
        url = request.POST.get('url', '')  # Get URL from form

        # Extract the post ID from the URL
        if url:
            parsed_url = urlparse(url)
            post_id = parsed_url.path.split('/')[-3] if '/comments/' in parsed_url.path else None

            if post_id:
                reddit = praw.Reddit(
                    client_id=settings.REDDIT_CLIENT_ID,
                    client_secret=settings.REDDIT_CLIENT_SECRET,
                    user_agent=settings.REDDIT_USER_AGENT
                )

                # Fetch the post using the post ID
                post = reddit.submission(id=post_id)
                post.comments.replace_more(limit=0)  # Replace "more comments" with actual comments

                # Initialize counters for sentiment analysis
                total_score = 0.0
                total_comments = 0
                positive_count = 0
                negative_count = 0

                # Loop through the comments and perform sentiment analysis
                for comment in post.comments.list():
                    comment_body = comment.body

                    # Check the length of the comment
                    if len(comment_body) > 512:
                        # Truncate the comment if it's too long
                        comment_body = comment_body[:512]

                    # Use the sentiment analysis model
                    sentiment = sentiment_pipeline(comment_body)

                    # Add the comment analysis to the posts list
                    posts.append({
                        "comment": comment_body,
                        "sentiment": sentiment[0]['label'],  # Get the sentiment label
                        "score": sentiment[0]['score'],      # Get the sentiment score
                        "sentiment_class": "positive" if sentiment[0]['label'] == 'POSITIVE' else "negative"  # Classify for CSS
                    })

                    # Update total score and count
                    total_score += sentiment[0]['score']
                    total_comments += 1

                    # Count positive and negative sentiments
                    if sentiment[0]['label'] == 'POSITIVE':
                        positive_count += 1
                    else:
                        negative_count += 1

                # Calculate weighted sentiment score
                weighted_score = total_score  # Positive scores are added, negative scores are subtracted

                # Determine overall sentiment
                if total_comments > 0:
                    if positive_count > negative_count:
                        overall_sentiment = f"Most users had a positive sentiment (score: {weighted_score:.2f})"
                    elif negative_count > positive_count:
                        overall_sentiment = f"Most users had a negative sentiment (score: {weighted_score:.2f})"
                    else:
                        overall_sentiment = f"Most users had a neutral sentiment (score: {weighted_score:.2f})"

    return render(request, 'sentiment/index.html', {'posts': posts, 'url': url, 'overall_sentiment': overall_sentiment})
