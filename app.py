from agent import research
from report import save_report
from pdf_report import save_pdf

print("=" * 50)
print("🤖 AI RESEARCH AGENT")
print("=" * 50)

while True:

    topic = input("\nResearch Topic (or 'exit'): ")

    if topic.lower() == "exit":
        print("Goodbye!")
        break

    report = research(topic)

    print("\n" + "=" * 50)
    print(report)
    print("=" * 50)

    md_path = save_report(topic, report)

    pdf_path = save_pdf(topic, report)

    print(f"\n✅ Markdown saved: {md_path}")

    print(f"✅ PDF saved: {pdf_path}")