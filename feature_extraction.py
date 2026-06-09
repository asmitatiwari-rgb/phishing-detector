from urllib.parse import urlparse
import re

def extract_features(url):
    parsed = urlparse(url)

    url_length = len(url)
    dot_count = url.count('.')
    hyphen_count = url.count('-')
    has_https = 1 if url.startswith("https") else 0

    special_chars = len(re.findall(r'[@#$%^&*()!?]', url))
    digit_count = sum(c.isdigit() for c in url)

    domain = parsed.netloc
    subdomain_count = domain.count('.')

    return [
        url_length,
        dot_count,
        hyphen_count,
        has_https,
        special_chars,
        digit_count,
        subdomain_count
    ]