import requests
from bs4 import BeautifulSoup

base_url = "https://www.amazon.sg/s?k=" # Base url link
search_item = input("Enter search input: ") # Search input
max_page = 20 # Set max number of pages

# Search from pages 1-max_page
for page in range(1, max_page+1, 1):
    url = base_url+search_item+"&page="+str(page) # Add page number to link
    req = requests.get(url) # Fetch url
    content = req.content # Read url
    soup = BeautifulSoup(content, "html.parser") # Parse html content
    all = soup.find_all("div", {"class": "s-result-item"}) # Find all search items in page

    # For every item in the page, do this
    for item in all:

        # Create an empty dictionary
        d= {}

        #Populate dictionary values with search results
        try:
            d["name"] = item.find("span", {"class": "a-text-normal"}).text
            d["price"] = item.find("span", {"class": "a-offscreen"}).text
            d["rating"] = item.find("span", {"class": "a-icon-alt"}).text
            print(d["name"],'\n',d["price"],'\n',d["rating"],'\n')
        except:
            pass

            
        
