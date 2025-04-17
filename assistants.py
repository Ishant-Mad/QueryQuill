import asyncio
from openai import OpenAI
import config
import os
import requests
import json
from bs4 import BeautifulSoup

news_api_key = config.news_api_key


# Function to scrape the website
def scrape_website(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = soup.find_all('p')
        content = "\n".join(f"<p>{p.get_text()}</p>" for p in paragraphs)
        
        # Wrap in basic HTML structure
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Scraped Content</title>
        </head>
        <body>
            {content}
        </body>
        </html>
        """
        
        return html_content
    else:
        return f"<p>Failed to retrieve content from {url}. Status code: {response.status_code}</p>"
    
def get_news(topic):
    """Get news information based on a given topic."""
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apikey={news_api_key}&pageSize=5"
    )
    try:
        response = requests.get(url)
        
        news = json.dumps(response.json(), indent=3)
        news_json = json.loads(news) 
        data = news_json
        
        articles = data["articles"]
        final_news = []
        
        for article in articles:
            source_name = article["source"]["name"]
            author = article["author"]
            title = article["title"]
            description = article["description"]
            url = article["url"]
            
            title_description = f""" 
                Title: {title},
                Author: {author},
                Source: {source_name},
                Description: {description},
                URL: {url}
            """
            final_news.append(title_description)
        return final_news
            
    except Exception as e:
        print("Something went wrong:", e)