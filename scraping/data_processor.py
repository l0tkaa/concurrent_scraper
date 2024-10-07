import multiprocessing
from bs4 import BeautifulSoup

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self, data_chunk):
        soup = BeautifulSoup(data_chunk, 'html.parser')
        # Perform the data extraction and processing here
        # For example: extract titles or links
        return soup.title.string if soup.title else "No title"

    def process_in_parallel(self):
        # Split the data into chunks for processing
        chunks = self._split_data_into_chunks(self.data)

        with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
            results = pool.map(self.process, chunks)
            for result in results:
                print(result)

    def _split_data_into_chunks(self, data, chunk_size=10000):
        # A utility function to split large data into chunks
        return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
