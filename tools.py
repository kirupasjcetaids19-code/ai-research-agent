from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_tool(query):
    
    
    
    
    0 print("\n🌐 Searching the Internet...")

    response = client.search(
        query=query,
        max_results=5
    )

    text = ""

    for item in response["results"]:

        text += f"""
Title: {item['title']}

Content:
{item['content']}

URL:
{item['url']}

--------------------------------
"""

    return text