import requests
from bs4 import BeautifulSoup as bss4
import csv


with open("products.csv" , 'a'  , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name" , "Price" , "Rating"])
    for i in range(20):
        url = requests.get(f"https://www.amazon.eg/-/en/s?i=electronics&rh=n%3A21832883031&fs=true&page={i}&language=en&qid=1655808699&ref=sr_pg_2")
        soup =bss4(url.text,"lxml" )

        products_title = soup.findAll("div" , {"class" : ["s-card-container","s-latency-cf-section"]})
        
        for product in products_title:
            try:
                title=product.find("span" , {'class' : ['a-size-base-plus',"s-line-clamp-4" , "a-spacing-none"]}).text
                price = product.find('span' , {'class' : "a-price-whole"}).text
                rating = product.find('span' , {'class' : ["a-size-base" , "s-underline-text"]}).text
                print({"title" : title,"price" : price , "rating" : rating
                })
                writer.writerow([title , price , rating])
            except Exception as e:
                print(str(e))
