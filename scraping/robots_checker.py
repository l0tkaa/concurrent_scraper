import requests
from urllib.parse import urljoin, urlparse

class RobotsChecker:
    def is_allowed_to_scrape(self, url):
        parsed_url = urlparse(url)
        robots_url = urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", "/robots.txt")
        
        try:
            response = requests.get(robots_url)
            if response.status_code == 200:
                disallowed_paths = self._parse_robots(response.text)
                return not any(urlparse(url).path.startswith(path) for path in disallowed_paths)
            return True
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return False
    
    def _parse_robots(self, robots_txt):
        disallowed_paths = []
        for line in robots_txt.splitlines():
            if line.startswith("Disallow"):
                disallowed_path = line.split(":")[1].strip()
                disallowed_paths.append(disallowed_path)
        return disallowed_paths
