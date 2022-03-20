import requests
from bs4 import BeautifulSoup
""" 
Get a value from specific website with Beautiful Soup https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Steps:

    1 - Pulling data out of HTML from specific website with Beautiful Soup
    2 - Parse data and get the desired value searching into the html parsed document
        In our case, we are finding a <div> with the class="val" <div class="val">value</div> We know that is the first div with that class in the html document.
    3 - Get the value with 'text'
    4 - Print some custom data with the obtained value.
"""
value = ''

#the url where do we get the data
url = "https://www.dolarhoy.com/"


try:
    response = requests.get(url)

    #Pulling data out of HTML from specific website with Beautiful Soup
    soup = BeautifulSoup(response.text, 'lxml')
    
    #Parse data and get the desired value searching into the html parsed document
    value = soup.find("div", {"class":"val"}).text

except requests.exceptions.RequestException as e:
    raise SystemExit(e)

print("the current value of the Dollar in Argentina is: $ARS: ", value, " = $USD 1")
#the current value of the Dollar in Argentina is: $ARS:  $199.5  = $USD 1

input("press Enter to exit..")

exit()
