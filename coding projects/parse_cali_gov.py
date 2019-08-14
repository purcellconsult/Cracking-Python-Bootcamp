########################################
# Parse the cali state site
# -------------------------
# A simple tutorial to get us
# comfortable with parsing websites
# for specific data using BS4.
#
# By Doug Purcell
# http://www.purcellconsult.com
#
########################################

from site_downloader import download

soup = download('https://www.ca.gov')

# header text
# select is used for css selectors

print('----- header anchor text -----')
for header_text in soup.select('span.link-title'):
    print(header_text.text)
print()

# header links
print('----- header links -----')
for a_href in soup.find_all('a', 'first-level-link'):
    print(a_href['href'])

print()
print('------- h4 and h3 text --------')
print()

# Gets the text in between a h4 tag with a certain class
for h4_text in soup.find_all('h4', attrs={'class': 'title'}):
    print(h4_text.text)

# Gets the text in between a h3 tag with a certain class
for h3_text in soup.find_all('h3', attrs={'class': 'title'}):
    print(h3_text.text)


print('---- footer text ----')
print(soup.select('span'))

# h2 module headers
for h2_text in soup.select('h2.et_pb_module_header'):
    print(h2_text.text, end=' | ')
print()

print()
print('----- more footer links -----')
list_stand_out = soup.select('.list-standout')
for list_items in list_stand_out:
    for x in list_items.find_all('a'):
        print(x['href'])


print()
print('----- website image links -----')

for images in soup.find_all('img'):
    print(images['src'])


print()
print('----- footer links -----')
for footer_links in soup.find_all('ul', {'class': 'footer-links'}):
    for links in footer_links.find_all('a'):
        print(links['href'])

print()
print('----- social sharing buttons -----')
social_buttons = soup.select('.socialsharer-container')
for social_links in social_buttons:
    links = social_links.find_all('a')
    for social in links:
        print(social['href'])

print(soup.select('.NaturalImage-imag'))