import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qurl = 'https://books.toscrape.com/'

qheader = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36'
}

qresp = rq.get(url = qurl, headers= qheader)

bsoup = BeautifulSoup(qresp.content , 'html.parser')

def convertNum(txNum):
    if txNum == 'One':
      return 1
    elif txNum == 'Two':
       return 2
    elif txNum == 'Three':
       return 3
    elif txNum == 'Four':
       return 4
    elif txNum == 'Five':
       return 5
    else:
       return 0

books_data = []

all_art = bsoup.find_all('article', {'class':'product_pod'})

for b in all_art:
    
    title = b.h3.a.attrs.get('title')
    
    rating_class = b.p.attrs.get('class')[1]
    rating = convertNum(rating_class) 
    
    price = b.h3.next_sibling.next_sibling.p.getText()
    
    books_data.append({
        'Title': title,
        'Rating': rating,
        'Price': price
    })

print(books_data)
