import bs4

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Advanced-Computer-Eyewear/SubCategory/ID-774?Tid=168113"
# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, price, shipping \n"
f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]
    if brand is None:
        brand = "No Brand"

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    price_container = container.findAll("li", {"class": "price-current"})
    price = price_container[0].text.strip()

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    
    print("brand: " + brand)
    print("product_name: " + product_name)
    print("price: " + price)
    print("shipping: " + shipping)

    f.write = (brand + "," + product_name.replace(",", "|") + "," + price + "," + shipping + "\n")

