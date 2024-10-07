import concurrent.futures
from scraping.scraper import Scraper
from scraping.data_processor import DataProcessor

def main():
    urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

    # Initialize Scraper with multithreading for scraping
    scraper = Scraper()
    
    # Create a thread pool for scraping
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(scraper.scrape, url): url for url in urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
                print(f"Scraped {url} successfully.")
                # Process the data in parallel using multiprocessing
                data_processor = DataProcessor(data)
                data_processor.process_in_parallel()
            except Exception as exc:
                print(f"{url} generated an exception: {exc}")

if __name__ == '__main__':
    main()
