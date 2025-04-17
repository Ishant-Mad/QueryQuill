# QueryQuill

Revolutionize how you find and use information with intelligent search and comprehensive content analysis.

## Overview

QueryQuill is a Streamlit application that integrates OpenAI's assistance API (Version 2) to create an intelligent assistant capable of interacting with uploaded documents, scraping web content, and fetching the latest news based on user-defined topics. The application is designed to assist users in various tasks such as researching topics, analyzing content, and staying updated with current events.

### Key Features

- **File Upload and Search**: Upload multiple files (PDFs, research papers, etc.) and store them in a vector database. The assistant can then answer questions related to these files.
- **Web Scraping**: Enter a URL to scrape content from a website. The scraped content is stored in the vector database, and users can ask questions related to the content.
- **News Fetching**: Get the latest news on a given topic with details such as the title, author, description, and URL to the news source.
- **Intelligent Assistant**: Powered by OpenAI's `gpt-4o-mini` model, the assistant uses a combination of tools (file search, code interpreter, web scraping, news fetching) to answer user queries.

## Installation

To install and run this application locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Abhishekwagh20/insightai-suite.git
    cd insightai-suite
    ```

2. **Set up a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure API keys**:

    - Create a `config.py` file in the project directory and add your OpenAI API key and News API key:

    ```python
    API_KEY = "your-openai-api-key"
    news_api_key = "your-news-api-key"
    ```

5. **Run the application**:

    ```bash
    streamlit run app.py
    ```

6. **Access the application**:

    Open your web browser and navigate to `http://localhost:8501` to interact with the application.

## Usage

### Creating an Assistant

1. **Enter a Title**: This will be the name of your assistant session.
2. **Initiate the First Question**: Provide a prompt to start the conversation with the assistant.
3. **Upload Files**: Upload any files you want the assistant to reference. These files will be stored in a vector database for search and retrieval.
4. **Ask Questions**: Once the assistant is initialized, you can ask follow-up questions related to the uploaded files or other content.

### Web Scraping and News Fetching

- **Web Scraping**: Provide a URL, and the assistant will scrape the content and store it. You can then ask questions related to the content.
- **News Fetching**: Provide a topic, and the assistant will fetch the latest news articles related to that topic.

### Example Use Cases

- **Research and Study**: Upload research papers and websites related to a subject, and ask the assistant to summarize and provide insights.
- **Job Preparation**: Upload resumes and company profiles to receive tailored advice on job applications and interview preparation.

## Requirements

- Python 3.7+
- Streamlit
- Claude API Key
- News API Key

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.





