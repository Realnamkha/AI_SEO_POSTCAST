from dotenv import load_dotenv
import openai
import json
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Set API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

# Set the model name, default to gpt-4-turbo if not set
model_name = os.getenv("OPENAI_MODEL_NAME", "gpt-4-turbo")

# Read JSON data from file
with open('extracted_articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Convert JSON data to a string
json_string = json.dumps(articles, indent=4)

# Define the prompt for summarization
prompt = '''
Please write a podcast script for a weekly SEO update from a digital marketing company from the articles I will provide. The script should be informative and engaging, covering the latest trends and developments in the SEO space. Include an introduction, brief company overview, main content with four recent SEO topics, and a closing call to action.

Details to include:
Company Name: ACERO
Company Description: A UK-based data-driven digital marketing company focusing on SEO and content marketing.
Closing: Encourage listeners to follow and subscribe on YouTube and visit the company's website for more information.

List of articles:

{json_string}

Words to Avoid:
   - plethora
   - blend
   - intricacies
   - symphony
   - myriad
   - seasoned
   - daunting task
   - bustling
   - sprawling
   - navigating
   - unlocking
   - remarkable proficiency
   - cutting-edge
   - navigate
   - tapestry
   - uncover
   - discover
   - delve
   - intriguing
   - dive deep into
   - encapsulates
   - intersection
   - seasoned
   - sprawling
   - navigating
   - at its heart
   - embark
   - dissect
   - intricate
   - cohesive
   - transcends
   - prowess
   - labyrinth
   - beacon
   - maze
   - forefront
   - pathway
   - realm
   - overstated
   - ascend
   - elevate

OUTPUT

Podcast Script for ACERO's Weekly SEO Update

[🎵 Intro Music]

"Welcome to this week’s episode of 'SEO Insights,' brought to you by ACERO, your go-to digital marketing ally. We're a UK-based company dedicated to demystifying SEO and content marketing through data-driven strategies. Each week, we dive into the latest trends and shifts in the SEO landscape, ensuring you stay ahead of the curve. Today, we're unpacking four fascinating developments from the world of search engine optimization."

[Segment Intro]

"Let’s kick things off with a look at what’s been happening this week in SEO!"

[Main Content]

1. **[Title of Article 1]**
   "First up, we've got some interesting updates on [brief description of Article 1]. Here’s what you need to know: [Summarize key points from Article 1]. This highlights the importance of [conclusion or action point from Article 1]."

2. **[Title of Article 2]**
   "Moving on, [brief description of Article 2]. It’s fascinating to see how [Summarize key points from Article 2]. For businesses, this means [conclusion or action point from Article 2]."

3. **[Title of Article 3]**
   "Next, we look at [brief description of Article 3]. This article brings to light [Summarize key points from Article 3]. The takeaway here is [conclusion or action point from Article 3], which is crucial for any SEO strategy."

4. **[Title of Article 4]**
   "Lastly, we discuss [brief description of Article 4]. The main points include [Summarize key points from Article 4], impacting how we approach [conclusion or action point from Article 4]."

[🎵 Segment Outro]

"And that wraps up our main content for today’s episode. We hope you found these insights helpful and that they add value to your SEO efforts."

[🎵 Closing]

"Before we sign off, a reminder to all our listeners: if you enjoyed today’s content, don’t forget to follow and subscribe to our podcast on YouTube. For more detailed insights, articles, and resources, visit our website at [ACERO's website URL]. We're here to help you excel in the dynamic world of digital marketing."

"Thanks for tuning in to 'SEO Insights.' We look forward to bringing you more updates next week. Until then, keep optimizing and stay ahead!"

[🎵 Outro Music]

"Have a great week, everyone!"
'''





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

# Extract the response content
content =  response.choices[0].message.content
print(content)

# Save the summary to a text file
with open('main.txt', 'w', encoding='utf-8') as f:
    f.write(content)

print("Summary has been saved to 'main.txt'")

# Text-to-Speech conversion using ElevenLabs

# Import necessary librari