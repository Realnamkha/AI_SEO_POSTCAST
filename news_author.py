import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def get_news_url():
    category_url = "https://www.searchenginejournal.com/category/news/"
    headers = {"User-Agent": "Mozilla/5.0"}  # Example header, adjust as needed

    response = requests.get(category_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the div with the id 'archives-wrapper'
    archives_wrapper = soup.find("div", {"id": "archives-wrapper"})
    
    # Ensure the div is found
    if not archives_wrapper:
        print("archives-wrapper not found")
        return {}

    # Find all articles within the div
    articles = archives_wrapper.find_all('article')
    
    if not articles:
        print("No articles found")
        return {}

    articles_by_author = defaultdict(list)

    for article in articles:
        # Extract the author
        author_tag = article.find('a', class_='sej-art-aut')
        if not author_tag:
            continue
        
        author_name = author_tag.get('title', '').replace("Go to Author Page", "").strip()
        author_url = author_tag.get('href', '')

        # Extract the article link
        article_tag = article.find('a', title="Read the Article")
        if not article_tag:
            continue
        
        article_url = article_tag.get('href', '')
        article_title = article_tag.text.strip()

        # Group articles by author
        articles_by_author[(author_name, author_url)].append((article_title, article_url))

    return articles_by_author

# Get and print news URLs grouped by author
news_urls_by_author = get_news_url()
for (author, author_url), articles in news_urls_by_author.items():
    print(f"Author: {author} ({author_url})")
    for title, url in articles:
        print(f" - {title}: {url}")
