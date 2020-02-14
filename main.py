import requests
import bs4


def getData(asin):
    r = requests.get('https://www.amazon.it/gp/product/' + asin, headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0'})
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    return {'name': soup.find(id='productTitle').string.strip(), 'price': soup.find(id='price_inside_buybox').string.strip()}


if __name__ == '__main__':
    print(getData('B00C0Q3SQA'))
    print(getData('B0764LJ8KT'))
