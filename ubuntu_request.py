import requests
import os
from urllib.parse import urlparse
import hashlib
from concurrent.futures import ThreadPoolExecutor
from typing import List

class UbuntuImageFetcher:
    def __init__(self, output_dir: str = "Fetched_Images"):
        self.output_dir = output_dir
        self.downloaded_images = set()
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_image(self, url: str) -> bytes:
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
            return None

    def get_filename_from_url(self, url: str) -> str:
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename:
            filename = "downloaded_image.jpg"
        return filename

    def get_image_hash(self, content: bytes) -> str:
        return hashlib.md5(content).hexdigest()

    def save_image(self, content: bytes, filename: str) -> bool:
        try:
            with open(filename, 'wb') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"✗ An error occurred: {e}")
            return False

    def download_image(self, url: str) -> None:
        content = self.fetch_image(url)
        if content is None:
            return

        image_hash = self.get_image_hash(content)
        if image_hash in self.downloaded_images:
            print(f"✓ Skipping duplicate image: {url}")
            return

        self.downloaded_images.add(image_hash)

        filename = self.get_filename_from_url(url)
        filepath = os.path.join(self.output_dir, filename)

        if self.save_image(content, filepath):
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        else:
            print(f"✗ Failed to save image: {url}")

    def download_images(self, urls: List[str]) -> None:
        with ThreadPoolExecutor() as executor:
            executor.map(self.download_image, urls)

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    fetcher = UbuntuImageFetcher()
    urls = input("Please enter the image URLs (separated by commas): ").split(',')
    urls = [url.strip() for url in urls if url.strip()]

    fetcher.download_images(urls)
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
