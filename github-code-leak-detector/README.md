# GitHub Code Leak Detector

## Overview

This tool scans public GitHub repositories for accidental secret leaks such as API keys and tokens.

## Structure

- `scan_github.py` – Main scanner
- `patterns.py` – Regex patterns for detecting secrets
- `alert.py` – Email alerting system
- `dashboard.py` – Optional Streamlit dashboard for displaying results

## Setup

1. Get a GitHub personal access token.
2. Set up email credentials for Gmail (use App Password if 2FA is enabled).
3. Edit credentials in `scan_github.py` and `alert.py`.
4. Run the script:

```bash
python scan_github.py
```

## Features

- Regex-based secret detection
- Real-time scanning of public GitHub code
- Email alerts for each detection
- Optional dashboard display

---