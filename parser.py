import urllib.request

def parse_html(html):
    pass

def parse_url(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        return parse_html(html)
