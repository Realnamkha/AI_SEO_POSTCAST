import requests
from bs4 import BeautifulSoup

def get_news_articles():
    category_url = "https://www.searchenginejournal.com/category/news/"
    headers = {"User-Agent": "Mozilla/5.0"}  # Example header, adjust as needed

    response = requests.get(category_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the div with the id 'archives-wrapper'
    archives_wrapper = soup.find("div", {"id": "archives-wrapper"})
    
    # Ensure the div is found
    if not archives_wrapper:
        print("archives-wrapper not found")
        return []

    # Find all articles within the div
    articles = archives_wrapper.find_all('article')
    
    if not articles:
        print("No articles found")
        return []

    article_links = []

    for article in articles:
        # Extract the article link
        article_tag = article.find('a', title="Read the Article")
        if not article_tag:
            print("Article tag not found for an article")
            continue
        
        article_url = article_tag['href']
        article_title = article_tag.text.strip()

        # Append the article title and URL to the list
        article_links.append((article_title, article_url))

    return article_links

# Get and print news article titles and URLs
news_articles = get_news_articles()
for title, url in news_articles:
    print(f"{title}: {url}")
