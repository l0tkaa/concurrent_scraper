import re
from urllib.parse import urlparse

def is_valid_url(url):
    """Validate a URL using regex."""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def extract_title(html_content):
    """Extract the title from HTML content."""
    match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    return match.group(1) if match else None

def parse_query_string(query_string):
    """Convert a query string to a dictionary."""
    if query_string:
        return dict(param.split('=') for param in query_string.split('&'))
    return {}

def clean_text(text):
    """Remove extra whitespace and non-printable characters from text."""
    return ' '.join(text.split()).strip()

def get_base_url(url):
    """Extract the base URL from a given URL."""
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"
