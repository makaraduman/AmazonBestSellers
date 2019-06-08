import requests

from bs4 import BeautifulSoup

url = "https://www.amazon.com/Best-Sellers/zgbs"

response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Enter Your Rating:"))


title = soup.find_all("li",{"class":"p13n-sc-truncated"})
rating = soup.find_all("td",{"class","a-size-small a-link-normal"})


for title, rating in zip(title,ratingler):
    title = title.text
    rating = rating.text

    title = title.strip()
    title = title.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > a):
        print("Product Name: {} Product Rating : {}".format(title,rating))

