###############################################
# Simple BS4 tutorial
# -------------------
#
# Learn the basics of parsing with bs4
# by parsing sightseeingpass:
# https://www.sightseeingpass.com/en/new-york
#
# By Doug Purcell
# http://www.purcellconsult.com
#
###############################################

from site_downloader import download


site = download('https://www.sightseeingpass.com/en/new-york')

prettify = site.prettify()
# print(prettify)

print('---- title tag in page ----')
print(site.title)

print()
print('---- title tag string -----')
print(site.title.string)
print()

print('---- title parent name ----')
print()
print(site.title.parent.name)
print()

print('----- body tag -----')
print(site.body)
print()

print('----- meta tag -----')
print(site.meta)
print()

# gets all of the script tags
print('----- script tags -----')
script_tags = site.find_all('script')
print(script_tags)
print('--- script tag ends ---')

# gets all ul tags
print('----- ul tags -----')
ul_tags = site.find_all('ul')
print(ul_tags)
print('----- ul tags end -----')
print()

# gets all of the li tags
print('----- li tags -----')
li_tags = site.find_all('li')
print(li_tags)
print('----- li tags ends -----')
print()

# gets all of a tags
print('----- a tags ----- begin')
a_tags = site.find_all('a')
print(a_tags)
print('----- a tags ----- end')

# gets all of the p tags
print('----- p tag ------')
p_tag = site.find_all('p')
print(p_tag)
print('-----p tag ends ------')
print()

# get all of the img tags
print('----- img tag ------')
img_tag = site.find_all('img')
print(img_tag)
print('----- img tag ends ------')
print()

# gets all of the button tags
print('----- button tag ------')
button_tag = site.find_all('button')
print(button_tag)
print('----- button tag ends ------')
print()

# div tag
print('----- div tag ------')
div_tag = site.find_all('div')
print(div_tag)
print('----- div tag ends ------')
print()

# span tag
print('----- span tag -----')
span_tag = site.find_all('span')
print(span_tag)
print('----- span tag end -----')
print()

# do you see a pattern on how to get all of a certain html tag?

# Counting tags in bs4
# ---------------------------
# count number of <br /> tags
# count number of i tags
# count the number of u tags
# count the number of b tags
# count the number of div tags

br_count = 0
for br_tag in site.find_all('br'):
    br_count += 1

i_tag_count = 0
for i_tag in site.find_all('i'):
    i_tag_count += 1

u_tag_count = 0
for u_tag in site.find_all('u'):
    u_tag_count += 1

b_tag_count = 0
for b_tag in site.find_all('b'):
    b_tag_count += 1


print('---- Div Tag Count ----')
div_tag_count = 0
div_count = len(site.find_all('div'))

print('There\'s {} br tags'.format(br_count))
print('There\'s {} i tags'.format(i_tag_count))
print('There\'s {} u tags'.format(u_tag_count))
print('There\'s {} b tags'.format(b_tag_count))
print('There\'s {} div tags'.format(div_count))


# refining our bs4 scraps
# -----------------------
# most scraps aren't this simple
# sometimes we get data that we don't want
# therefore, we need ways to extract only certain parts


# find method
# ------------
# function signature: find(name, attrs, recursive, string, **kwargs)
# details: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find
# compared to find_all it just looks for the first result. find_all
# scans the entire document looking for results. I.e, tags that
# occur once like body, html, head, title, etc.
# Also, find returns the result, while find_all returns a list of results

print('----- The header -----')
header = site.find('header')
print('The header is {}'.format(header))
print('----- The header end -----')
print()

print('----- div slice -----')
div_tags = site.find_all('div')
print(div_tags[1:4])
print('----- div slice end -----')
print()

# select
# ------
# css selectors
# select, match, filter using modern CSS selectors
# learn about the api: https://facelessuser.github.io/soupsieve

print('----- regular match with css selectors -----')
print(site.select('title'))
print()

print('----- find tags beneath other tags -----')
top_10_nyc = site.select('p span')
print(top_10_nyc)

# how to refine so i get the span tag with the class attribute...
# of menu-hover-bar--red?
top_10_nyc = site.select(".menu-hover-bar--red")[0]
print(top_10_nyc)

# how can we get the text between the tags?
print(top_10_nyc.get_text())

# what's a second way that I can get text between tags?
# get the first element from the contents
print(top_10_nyc.contents[0])

# what's a 3rd way :-)?
# find the next tag, use next attribute
print(top_10_nyc.next)

# jeez, what's a fourth way?
# use .string
print(top_10_nyc.string)
print()

print('----- find tags directly beneath other tags -----')
site_lists = site.select('p > span')
for x, y in enumerate(site_lists):
    print(site_lists[x].contents[0])
print()

print('----- Address -----')
contact_us = site.select('.desk-footer__contact-us p')
print(contact_us[0].get_text())

print('----- Get the a tags in the footer -----')
footer_links = site.select('#linksMoreInformation a')
for links in footer_links:
    print(links)
print()
print('----- Get the href tags in the footer -----')
for links in footer_links:
    print(links['href'])
print()

print('----- Get the social media links -----')
for social_links in site.select('.social-bar li a'):
    print(social_links['href'])

print()
print('----- get all of the links on the site -----')
for web_links in site.find_all('a', {'href': True}):
    print(web_links['href'])


# understanding parents and siblings
# ----------------------------------

# parents is needed if you need to work your way up a tree
# i.e, start somewhere and then start working your way up
print()
print('----- parents -----')
print()

tag = site.find('head')
print(tag.find_parents('html'))
print()

# gets elements that's side by side
print('----- siblings -----')
div_class = site.find('div')
print(div_class.find_next_sibling())
