from dotenv import load_dotenv
import openai
import json
import os

# Load environment variables from .env file
load_dotenv()

# Set API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the model name
model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4-turbo")  # Default to gpt-4-turbo if not set

# Read JSON data from file
with open('extracted_articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Convert JSON data to a string
json_string = json.dumps(articles, indent=4)

# Define the prompt for summarization
prompt = f"Please provide a detailed summary of the following articles. Include key insights, main points, and any significant details.The total summary should be at least 1500 words:\n\n{json_string}"


# Call the OpenAI API for summarization using the ChatCompletion method for gpt-4-turbo
response = openai.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=3500,  # Adjust token limit as needed
    temperature=0.5
)

# Print the response object type and attributes to understand its structure
content = response.choices[0].message.content
print(content)

# Save the summary to a text file
with open('summary.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("Summary has been saved to 'summary.txt'")
