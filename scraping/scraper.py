import requests
import threading
from scraping.rate_limiter import RateLimiter
from scraping.proxy_manager import ProxyManager
from scraping.logger import ScrapingLogger
from scraping.session_manager import SessionManager

class Scraper:
    def __init__(self, logger=None, rate_limiter=None, session_manager=None, proxy_manager=None):
        self.logger = logger or ScrapingLogger()
        self.rate_limiter = rate_limiter or RateLimiter()
        self.session_manager = session_manager or SessionManager()
        self.proxy_manager = proxy_manager or ProxyManager()

    def scrape(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        proxy = self.proxy_manager.get_next_proxy() if self.proxy_manager else None

        if proxy:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy})
        else:
            response = self.session_manager.get(url, headers)

        if response.status_code == 200:
            self.logger.log_request(url, response.status_code)
            return response.text
        else:
            self.logger.log_request(url, response.status_code)
            return None

        # Make sure we respect the rate limit
        self.rate_limiter.wait()
