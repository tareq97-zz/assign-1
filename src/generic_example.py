from ast import arg
from urllib import response
from urllib.request import urlopen
import os
import requests
import lxml
from bs4 import BeautifulSoup
import validators
from bs4 import ResultSet

import argparse

sourceFile = open('headers_links.txt', 'w')

def open_print_to_source(message):  
  print(message, file = sourceFile)

def close_source():
  sourceFile.close()

def all_headers_links(website):
  links = ResultSet(None) 
  valid=validators.url(website)
  #print("Name of the Website ::::" + str(website))
  #print("This is validation part :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" + str(valid))
  if valid==True:
    #print("Valid was TRUE :::::::::::::::::::::::::::::::::::::::::::::")
    r = requests.get(website,verify=True)
    html = r.text
    bs = BeautifulSoup(html, "html.parser")
    titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
    name = "<a>" + website + "</a>"
    summary = "<br>summary:"
    open_print_to_source(name)
    open_print_to_source(summary)

    if not titles:
      print("<br>--> Does not contain headers on this page")
      open_print_to_source("<br>--> Does not contain headers on this page")
    for y in titles:
      if y.name == "h1":
        print("# ----> " + y.text)
        open_print_to_source("# " + y.text)
      elif y.name == "h2":
        print("## ----> " + y.text)
        open_print_to_source("## " + y.text)
      elif y.name == "h3":
        print("### ----> " + y.text)
        open_print_to_source("### " + y.text)
      elif y.name == "h4":
        print("#### ----> " + y.text)
        open_print_to_source("#### " + y.text)
      elif y.name == "h5":
        print("##### ----> " + y.text)
        open_print_to_source("##### " + y.text)
      elif y.name == "h6":
        print("###### ----> " + y.text)
        open_print_to_source("###### " + y.text)
  
    links = bs.find_all('a')

    for y in links:
      if y.get('href') is not None:
        print(y['href'])
        open_print_to_source(y['href'])
  else:
    print("<br>--> broken link <a>" + website + "</a>")
  
    #print
  return links

def tree(link, website, depth):
  if depth <= 0:
    return None
  else:
    links = ResultSet(source=None)
    #links = all_headers_links(website + link['href'])
    links = all_headers_links(website)
    depth = depth - 1
    for x in links:
      tree(x, website, depth)
    return links

def go_main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--website",type=str, required=True)
  parser.add_argument("--depth",type=int, required=True)
  args = parser.parse_args()
  print('Website: ', args.website)
  print('Depth: ', args.depth)

  name = "<a>" + args.website + "</a>"
  depth = "<br>depth:" + str(args.depth)
  summary = "<br>summary:"

  #links = all_headers_links(args.website) 
  tree_link = all_headers_links(args.website)
  depth1 = args.depth - 1 
  for x in tree_link:
    tree(x,args.website,depth1)

  close_source()

go_main()