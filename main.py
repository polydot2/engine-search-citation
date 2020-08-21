import requests
import time
import os
import sys
from bs4 import BeautifulSoup
import lxml
import csv
import json

list_citations = []
list_themes = []
url="https://www.abc-citations.com/themes"
list_url_theme = []
reponse = requests.get(url) #search all theme
print ('ok')
if reponse.ok:
    print("ok")
    content_html = reponse.text
    soups = BeautifulSoup(content_html, "lxml")
    #find all url theme citations
    soups = soups.find("ul", {'id':'list-themes'})
    themes = soups.find_all('a')
    print(themes)
    #iterer les les elements
    for theme in themes:
        url_theme = theme.get('href') 
        name_theme = theme.find('span', {'class':'name'}).get_text()
        number_citation_theme = theme.find('span', {'class':'number'}).get_text()

        print(" |||= url theme :",url_theme)
        print(" |||= name theme :",name_theme)
        print(" |||= number :",number_citation_theme)
        item_theme ={
            "url theme":url_theme,
            "name theme":name_theme,
            "number":number_citation_theme
        }
        list_url_theme.append(url_theme)
        list_themes.append(item_theme)

#save list theme json
with open("theme_citation.json","w",encoding="utf-8") as flux_json:
    json.dump(list_themes,flux_json,indent=4)

#save liste theme csv
with open("theme_citation.csv","w",encoding="utf-8") as flux_csv:
    fieldnames = ['url theme', 'name theme', 'number']
    writer = csv.DictWriter(flux_csv, fieldnames=fieldnames)
    writer.writeheader()
    for theme in list_themes:
        writer.writerow(theme)

list_citations = []

for url_cit in list_url_theme:
    reponse = requests.get(url_cit)

    if reponse.ok:

        content_html = reponse.text
        soups = BeautifulSoup(content_html, 'lxml')
        soup = soups.find_all('article')
        next_page = soups.find('a', {'class':'nextpostslink'})

        while next_page:

            for item_article in soup:
                citation = item_article.find('p', {'class':'quote'}).get_text().replace('\"','').replace('"','')
            author = item_article.find('a').get_text()
            book = item_article.find('p', {'class':'book'}).get_text().replace('\t','').replace('\n','') if item_article.find('p', {'class':'book'}) else ''

            item_citation ={
                "citation":citation,
                'author':author,
                'book':book,
            }
            print( "|||= citation :", citation)
            print(" |||= author :",author)
            print(" |||= book :",book)

            list_citations.append(item_citation)
            page_next = next_page.get('href')
            reponse = requests.get(page_next)
            content_html = reponse.text
            soups = BeautifulSoup(content_html, 'lxml')
            soup = soups.find_all('article')
            next_page = soups.find('a', {'class':'nextpostslink'}) if soups.find('a', {'class':'nextpostslink'}) else False




        

#save liste citation json
with open("citations.json","w",encoding="utf-8") as flux_json:
    json.dump(list_citations,flux_json,indent=4)

#save liste citation csv
with open("citations.csv","w",encoding="utf-8") as flux_csv:
    fieldnames = ['citation', 'author', 'book']
    writer = csv.DictWriter(flux_csv, fieldnames=fieldnames)
    writer.writeheader()
    for citation in list_citations:
        writer.writerow(citation)

print(json.dumps(list_citations))

print(len(list_citations))

