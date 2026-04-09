import requests

ALLOWED_DOMAINS = [
    "github.com",
    "pypi.org",
    "docs.python.org"
]

def fetch(url):

    if not any(domain in url for domain in ALLOWED_DOMAINS):
        raise PermissionError("Domain not allowed")

    response = requests.get(url, timeout=10)

    return response.text