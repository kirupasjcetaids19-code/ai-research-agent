import os
from datetime import datetime

def save_report(topic, content):

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    filename = topic.replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = f"outputs/{filename}_{timestamp}.md"

    with open(filepath, "w", encoding="utf-8") as file:

        file.write(f"# {topic}\n\n")
        file.write(content)

    return filepath