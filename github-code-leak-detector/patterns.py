PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws_secret_access_key.*[=:]['\"]?([A-Za-z0-9/+=]{40})['\"]?",
    "Slack Token": r"xox[baprs]-[A-Za-z0-9-]+",
    "Private Key": r"-----BEGIN(.*?)PRIVATE KEY-----",
    "Generic API Key": r"(?i)(api_key|apikey|secret|token)[\"'\s:=]+[A-Za-z0-9_\-]{16,}",
    "Database URI": r"(mongodb|postgres|mysql)://[^\s]+"
}
