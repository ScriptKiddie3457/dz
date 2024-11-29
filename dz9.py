import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

book_titles = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("h3")
    for book in books:
        title = book.a["title"]
        book_titles.append(title)

for idx, title in enumerate(book_titles, 1):
    print(f"{idx}. {title}")

print("----------------------------")

book_cost = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    prices = soup.find_all("p", class_="price_color")
    for price in prices:
        book_cost.append(price.text)

for idx, cost in enumerate(book_cost, 1):
    print(f"{idx}. {cost}")

print("----------------------------")

books_data = []

for page in range(1, 51):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]

        books_data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
        })

for idx, book in enumerate(books_data, 1):
    print(
        f"{idx}. Name: {book['title']}, Cost: {book['price']}, Available: {book['availability']}, Rating: {book['rating']} star")