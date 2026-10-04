from chatbot import ask_ai
from tools import search_tool

def research(query):

    print("\n🧠 Thinking...")

    search_results = search_tool(query)

    prompt = f"""
You are an expert AI Research Assistant.

Research Topic:
{query}

Latest Search Results:
{search_results}

Create a professional report.

Include:

1. Introduction
2. Recent Developments
3. Advantages
4. Challenges
5. Future Scope
6. Conclusion

Write in simple English.
"""

    return ask_ai(prompt)