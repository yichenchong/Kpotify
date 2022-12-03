import hashlib
from concurrent.futures import ThreadPoolExecutor

from ...lib.requests import requests

import os

executor = ThreadPoolExecutor(max_workers=20)

cur_path = os.path.dirname(__file__)
temp_icons_path = os.path.join(cur_path, "temp_icons")


class ImageDownloaderConfig:
    def __init__(self):
        self.load_icons = False

    def get_load_icons(self):
        return self.load_icons

    def change_config(self, load_icons):
        self.load_icons = load_icons


image_downloader_config = ImageDownloaderConfig()


class ImageDownloader:
    """
    A class to download images in parallel.
    """
    @staticmethod
    def clear():
        for i in os.listdir(temp_icons_path):
            os.remove(os.path.join(temp_icons_path, i))

    @staticmethod
    def url_to_filename(url):
        return hashlib.md5(url.encode()).hexdigest() + ".jpg"

    @staticmethod
    def download(url):
        if url is None:
            return None
        filename = ImageDownloader.url_to_filename(url)
        return executor.submit(ImageDownloader._download, url, filename)

    @staticmethod
    def _download(url, filename):
        path = os.path.join(temp_icons_path, filename)
        resource_path = "res://Kpotify/src/kp_objects/temp_icons/" + filename
        if os.path.exists(path):
            return resource_path
        if image_downloader_config.get_load_icons():
            r = requests.get(url)
            with open(path, "wb") as f:
                f.write(r.content)
            return resource_path
        return None
