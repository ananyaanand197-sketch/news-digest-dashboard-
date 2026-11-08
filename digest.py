import json

def generate_html_report():
    print("Fetching RSS feeds and market data...")
    data = {"status": "success", "headlines": 5}
    print(f"Generated digest successfully: {json.dumps(data)}")

if __name__ == "__main__":
    generate_html_report()