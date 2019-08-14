############################################
# Requests site downloader in python
# ----------------------------------
#
# Includes custom user agent, exception
# handling, and automatic download retries.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
############################################

import requests
from bs4 import BeautifulSoup
from requests import RequestException, HTTPError, ConnectionError, URLRequired, TooManyRedirects


def download(url, tries=3):
    """
    This function downloads a site using request
    and also has some functionality in place to
    catch exceptions and do retries if the script
    didn't work.
    """

    # creates a user agent in requests
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    try:
        site = requests.get(url, headers=headers)
        soup = BeautifulSoup(site.text, 'lxml')
    except (RequestException, HTTPError, ConnectionError, URLRequired, TooManyRedirects) as e:
        print('Download error: {}'.format(e))
        if tries > 0:
            # recursive call until tries is 0
            return download(url, tries - 1)
    return soup

