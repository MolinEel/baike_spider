import urllib
from urllib import request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return
        response = urllib.request.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()
