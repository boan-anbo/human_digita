import requests
from bs4 import BeautifulSoup


def get_webpage_content_and_title(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    result = {}
    result['title'] = soup.title.text

    text = soup.find_all(text=True)

    content = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    for t in text:
        if t.parent.name not in blacklist:
            content += '{} '.format(t)

    result['content'] = content
    return result



# if __name__ == '__main__':
    # url = 'https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup'
    # get_webpage_content(url)
