<h1 align="center">🔐 GitHub Code Leak Detector</h1>

<p align="center">
  <img src="https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif" width="300" alt="Security Gif"/>
</p>

---

## 🚀 About the Project

A sleek and powerful tool to **detect sensitive data leaks** such as API keys, secrets, tokens, and passwords in public or private GitHub repositories using the **GitHub Search API** and regex matching.

This project showcases your **understanding of code security**, **regex pattern recognition**, and **monitoring digital footprint**.

---

## 🔍 Features

- 🕵️ Scans GitHub repos for keywords like `API_KEY`, `TOKEN`, etc.
- 🚨 Alerts when secret patterns are found
- 📊 Dashboard to view logs in real-time
- 🌐 Optional: Email notification integration
- 🔁 Custom regex pattern support
- 🧠 Fully customizable and modular

---

## 🛠️ Tech Stack

- 🐍 Python
- 🔎 GitHub REST API
- 🧪 Regex
- 🧮 Flask (Dashboard)
- 📤 SMTP (for optional email alerts)

---

## 📁 Project Structure

```
github-code-leak-detector/
├── scan_github.py       # Main scanner script
├── patterns.py          # Regex patterns for secrets
├── alert.py             # Alert handling (email/print/dashboard)
├── dashboard.py         # Real-time dashboard for leaks
└── README.md            # This beautiful README 😉
```

---

## 🧠 How It Works

1. **Authenticate** using your GitHub personal access token.
2. Search GitHub using keyword + optional user/org restriction.
3. Match file contents against secret regex patterns.
4. Display matched leaks in console and optional dashboard.

---

## ✅ Run it Locally

```bash
git clone https://github.com/YOUR_USERNAME/github-code-leak-detector.git
cd github-code-leak-detector
pip install -r requirements.txt
python scan_github.py
```

Make sure to update your GitHub token in the `scan_github.py` file.

---

## 📬 Want Email Alerts?

Update `alert.py` with your SMTP credentials and `send_alert()` will notify you immediately when leaks are found.

---

## 🧩 Customize Patterns

Add your own detection patterns to `patterns.py`:

```python
PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    ...
}
```

---

## 💡 Inspiration

> "Security is not a product, but a process." — Bruce Schneier

---

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2Y2NzFqeTZhZjR3Y2VzMHkyNzRucjF5ZnY3OXN2cnF2aDd1MGY0aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qgQUggAC3Pfv687qPC/giphy.gif" width="600" alt="demo-gif">
</p>

<p align="center">
  Made with ❤️ by <a href="https://github.com/SriVishnu-999">Sri Vishnu</a>
</p>
