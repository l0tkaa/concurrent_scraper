class ProxyManager:
    def __init__(self):
        self.proxies = ['http://proxy1.com', 'http://proxy2.com', 'http://proxy3.com']
        self.proxy_index = 0

    def get_next_proxy(self):
        proxy = self.proxies[self.proxy_index]
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        print(f"Using proxy: {proxy}")
        return proxy
