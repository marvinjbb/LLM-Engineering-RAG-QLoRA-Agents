from bs4 import BeautifulSoup                #lets python read and search through HTML - it helps turn messy HTML into usable text
import requests                              #lets python make HTTP requests 


# Standard headers to fetch a website - this header makes the request look like it came from a normal web browser beacuse many websites block blank or suspicious automated requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url):
    
    #Return the title and contents of the website at the given url and return only the first 2,000 characters 
    
    response = requests.get(url, headers=headers)                  #sending a GET request to the URL  asking for its page 
    soup = BeautifulSoup(response.content, "html.parser")          #turning HTML  into a Beautifulsoup object that python code can search 
    title = soup.title.string if soup.title else "No title found"  #getting the title
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):    #a for loop to find the given tags inside the page body and remove each one using decompose()
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True) #convert HTML into plain text
    else:
        text = ""                                             #if webpage doesnt have a body tag, set text to an empty string 
    return (title + "\n\n" + text)[:2_000]                    #return website title and text and only the first 2000 characters 


def fetch_website_links(url):
    
    # this function takes URLs and returns the webpage's links
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")] #list compreshension. a shorter way to build a list
    return [link for link in links if link]









from bs4 import BeautifulSoup
import requests


# Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


# class Website:
#     def __init__(self, url):
#         self.url = url
#         self.response = requests.get(url, headers=headers)
#         self.soup = BeautifulSoup(self.response.content, "html.parser")

#     def get_contents(self):
#         title = self.soup.title.string if self.soup.title else "No title found"

#         if self.soup.body:
#             for irrelevant in self.soup.body(["script", "style", "img", "input"]):
#                 irrelevant.decompose()

#             text = self.soup.body.get_text(separator="\n", strip=True)
#         else:
#             text = ""

#         return (title + "\n\n" + text)[:2000]

#     def get_links(self):
#         links = [link.get("href") for link in self.soup.find_all("a")]
#         return [link for link in links if link]


# # Create a Website object
# website = Website("https://example.com")

# # Call the methods
# print(website.get_contents())

# print(website.get_links())