
import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://readrate.com/rus'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
}


def get_html(url):
    request = requests.get(url, headers=HEADERS)
    return request

def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all("div", class_="book")
    top_list = []
    for item in items:
        title = item.find("div", class_="col-12 col-sm ml-sm-5").get_text(strip=True)
        image = URL + item.find("div", class_="book-picture float-left clearfix mb-2 mb-md-0").find("img").get("src")
        description = item.find("div", class_="book-description w-auto mt-2 mt-sm-3").get_text(strip=True)
        readers = item.find("div", class_="text-nowrap font-size-sm").get_text(strip=True)

        top_list.append(
            {
                "title": title,
                "image": image,
                "description": description,
                "readers": readers,
            }
        )

    return top_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        top_list2 = []
        for page in range(1,2):
            response = get_html("https://readrate.com/rus/ratings/top100")
            top_list2.extend(get_data(response.text))
        return top_list2
    else:
        raise Exception("error in parsing")


# print(parsing())


# import requests
# from bs4 import BeautifulSoup as BS4
#
# URL = 'https://www.chitai-gorod.ru/'
#
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
# }
#
#
# def get_html(url, params=""):
#     request = requests.get(url, headers=HEADERS, params=params)
#     return request
#
# def get_data(html):
#     bs = BS4(html, features="html.parser")
#     items = bs.find_all("div", class_="items-list")
#     labirint_list = []
#     for item in items:
#         title = item.find("div", class_="product-title__head").get_text(strip=True)
#         image = URL + item.find("div", class_="product-title__head").find("img").get("src")
#         author = item.find("ul", class_="product-title__author").get_text(strip=True)
#         price = item.find("ul", class_="product-price__value product-price__value--discount").get_text(strip=True)
#
#         labirint_list.append(
#             {
#                 "title": title,
#                 "image": image,
#                 "author": author,
#                 "price": price
#             }
#         )
#
#     return labirint_list
#
# def parsing():
#     response = get_html(URL)
#     if response.status_code == 200:
#         labirint_list2 = []
#         for page in range(1,2):
#             response = get_html("https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-110001", params={"page": page})
#             labirint_list2.extend(get_data(response.text))
#         return labirint_list2
#     else:
#         raise Exception("error in parsing")
#
#
# print(parsing())

# import requests
# from bs4 import BeautifulSoup as BS4
#
# URL = 'https://www.labirint.ru'
#
# HEADERS = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",
# }
#
#
# def get_html(url, params=""):
#     request = requests.get(url, headers=HEADERS, params=params)
#     return request
#
# def get_data(html):
#     bs = BS4(html, features="html.parser")
#     items = bs.find_all("div", class_="genres-carousel__container  products-row")
#     labirint_list = []
#     for item in items:
#         title = item.find("div", class_="genres-carousel__item").get_text(strip=True)
#         image = URL + item.find("div", class_="product-cover__cover-wrapper").find("img").get("src")
#         author = item.find("div", class_="product-author").get_text(strip=True)
#         price = item.find("div", class_="product-pricing").get_text(strip=True)
#
#         labirint_list.append(
#             {
#                 "title": title,
#                 "image": image,
#                 "author": author,
#                 "price": price
#             }
#         )
#
#     return labirint_list
#
# def parsing():
#     response = get_html(URL)
#     if response.status_code == 200:
#         labirint_list2 = []
#         for page in range(1,2):
#             response = get_html("https://www.labirint.ru/books/", params={"page": page})
#             labirint_list2.extend(get_data(response.text))
#         return labirint_list2
#     else:
#         raise Exception("error in parsing")
#
#
# print(parsing())


