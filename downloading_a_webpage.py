from urllib.request import urlopen

url  = "https://shopsearch.taobao.com/search?app=shopsearch&q=shoes"

response = urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)

from urllib.request import urlopen

url = "https://www.datacamp.com/community/tutorials/functions-python-tutorial"


def get_webpage(url):
    response = urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    return text

text = get_webpage(url)
print(text)


from urllib.request import urlopen

url  = "https://shopsearch.taobao.com/search?app=shopsearch&q=shoes"

def get_webpage(url):

    print("Getting Request Object")
    request = urlopen(url)
    print("Reading Request Object")
    data = request.read()
    text = data.decode("utf-8")

    print("Web Page Downloaded")
    return text

text = get_webpage(url)

                                                                                                                                     
with open('html_text.txt', 'w') as f:
    f.write(text)