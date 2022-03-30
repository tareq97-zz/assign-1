import requests
from bs4 import BeautifulSoup


def printHeader(website):
  
  #print("This is for next:")
  #print(website)
  #html = urlopen(website)

  r = requests.get(website)
  html = r.text
  bs = BeautifulSoup(html, "html.parser")
  titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
  if not titles:
    print("Does not contain headers on this page")
  links = bs.find_all('a')
  for y in titles:
    if y.name == "h1":
      print("# " + y.text)
    elif y.name == "h2":
      print("## " + y.text)
    elif y.name == "h3":
      print("### " + y.text)
    elif y.name == "h4":
      print("#### " + y.text)
    elif y.name == "h5":
      print("##### " + y.text)
    elif y.name == "h6":
      print("###### " + y.text)  
    else:
      print("Does not contain headers on this page")
  return links

#response = requests.get("https://campus.aau.at/")
#print(response)

printHeader("https://intranet.aau.at/")
