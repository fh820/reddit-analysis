# Reddit Sentiment Analysis

## Overview
This project performs sentiment analysis on Reddit comments using a natural language processing (NLP) model. It fetches comments from a given Reddit post, analyzes their sentiment, and provides an overview of the overall sentiment towards the topic discussed in the comments.

## Features
- Extract comments from a specified Reddit post.
- Analyze sentiment using a pre-trained DistilBERT model.
- Display sentiment results with confidence scores.
- Calculate the overall sentiment of the thread.

## Technologies Used
- Backend: Django
- NLP: Transformers (Hugging Face)
- Data Retrieval: PRAW (Python Reddit API Wrapper)
- Deployment: not yet 

## Installation
1. Clone this repository:
   git clone https://github.com/fh280/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis
2. Create a virtual environment and activate it
3. Install the required packages
4. Set up your Django settings with your Reddit API credentials:

     #In your Django settings.py file
     REDDIT_CLIENT_ID = 'your_client_id'
     REDDIT_CLIENT_SECRET = 'your_client_secret'
     REDDIT_USER_AGENT = 'your_user_agent'

5. Run the development server:
   python manage.py runserver

# Usage
Open your browser and navigate to http://127.0.0.1:8000/.
Enter the URL of a Reddit post you want to analyze and click "Analyze."
View the sentiment analysis results displayed on the page.
Contributing
Feel free to fork this repository and submit pull requests. Any contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Hugging Face for the Transformers library.
PRAW for the Reddit API wrapper.
