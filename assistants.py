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