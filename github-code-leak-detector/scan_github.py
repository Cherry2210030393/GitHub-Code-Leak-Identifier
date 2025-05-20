import requests
import re
import base64
from patterns import PATTERNS
from alert import send_alert

GITHUB_TOKEN = "you're_github_token"  
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def search_github(query):
    username = "Cherry2210030393"  
    url = f"https://api.github.com/search/code?q={query}+in:file+user:{username}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


def get_file_content(api_url):
    response = requests.get(api_url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        content = data.get("content", "")
        encoding = data.get("encoding", "")
        if encoding == "base64":
            try:
                decoded = base64.b64decode(content).decode("utf-8", errors="ignore")
                return decoded
            except Exception as e:
                print(f"[ERROR] Decoding content: {e}")
                return ""
    return ""

def check_for_secrets(code_text):
    findings = []
    for label, pattern in PATTERNS.items():
        matches = re.findall(pattern, code_text, re.IGNORECASE)
        if matches:
            findings.append((label, matches))
    return findings

def main():
    keywords = ["API_KEY", "SECRET", "TOKEN", "PASSWORD"]
    for keyword in keywords:
        print(f"\n🔍 Searching for keyword: {keyword}")
        data = search_github(keyword)
        items = data.get("items", [])
        for item in items:
            repo = item["repository"]["full_name"]
            file_url = item["html_url"]
            raw_url = item["url"]
            print(f"📄 Checking: {file_url}")
            content = get_file_content(raw_url)
            findings = check_for_secrets(content)
            if findings:
                for label, matches in findings:
                    alert_data = {
                        "type": label,
                        "match": matches[0],  
                        "repo": repo,
                        "url": file_url
                    }
                    print(f"🚨 ALERT: {label} found in {file_url}")
                    send_alert(alert_data)

if __name__ == "__main__":
    main()
