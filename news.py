import requests
from bs4 import BeautifulSoup
from newspaper import Article
import json

def get_news_articles():
    category_url = "https://www.searchenginejournal.com/category/seo/"
    headers = {"User-Agent": "Mozilla/5.0"}  # Example header, adjust as needed

    # Request the HTML content of the category page
    response = requests.get(category_url, headers=headers)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the div with the id 'archives-wrapper'
    archives_wrapper = soup.find("div", {"id": "archives-wrapper"})
    
    # Ensure the div is found
    if not archives_wrapper:
        print("archives-wrapper not found")
        return []

    # Find all <a> tags within the 'archives-wrapper' with the title attribute set to "Read the Article"
    article_tags = archives_wrapper.find_all('a', title="Read the Article")
    
    if not article_tags:
        print("No articles found")
        return []

    article_links = set()  # Use a set to avoid duplicates

    # Iterate over each <a> tag to extract the title and URL
    for article_tag in article_tags:
        if len(article_links) >= 10:
            break

        if 'href' not in article_tag.attrs:
            print("href attribute missing for an article")
            continue
        
        # Extract the URL from the href attribute
        article_url = article_tag['href']
        # Extract the title from the text content of the <a> tag
        article_title = article_tag.get_text(strip=True)

        # Use a tuple to store title and URL, and add it to the set
        article_links.add((article_title, article_url))

    return list(article_links)  # Convert back to a list

def get_article_content(article_url):
    # Initialize a newspaper Article object with the URL
    article = Article(article_url)
    # Download the article content
    article.download()
    # Parse the downloaded article content
    article.parse()
    # Return the title and text content of the article
    return article.title, article.text

# Get news article titles and URLs
news_articles = get_news_articles()

# Create a list to store all the extracted information
extracted_data = []

# Iterate over each title and URL pair
for title, url in news_articles:
    try:
        # Extract the title and content of the article
        article_title, content = get_article_content(url)
        
        # Use the title from the extracted article if it's more reliable
        if not title:
            title = article_title

        print(f"Title: {title}\nURL: {url}")
        print(f"Content: {content[:500]}...")  # Print first 500 characters for brevity
        
        # Append the extracted information to the list
        extracted_data.append({
            'title': title,
            'url': url,
            'content': content
        })
    except Exception as e:
        print(f"Failed to extract content for URL: {url}\nError: {e}")
    
    print("\n" + "="*80 + "\n")

# Save the extracted information to a JSON file
with open('extracted_articles.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=4)

print("Data has been saved to 'extracted_articles.json'")
