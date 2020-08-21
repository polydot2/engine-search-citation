# coding: utf-8
import requests
import time
import os
import sys
from bs4 import BeautifulSoup
import lxml
import csv


def author_citation(self):
    return self.text

list_citation=[]
list_auteur=[]
with open('mescitations.txt','w') as citf:
    citf.write('CITATIONS : \n AUTEUR :\n')
    for i in range(309):
        link = "https://www.ma-citation.com/p-"+str(i)
        reponse = requests.get(link)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text,'lxml')
            citations=soup.findAll('div',{'class':'divCitTxth2'})
            for citation in citations:
                cita=citation.find('h2',{'class':'txtCit'})
                cit=author_citation(cita)
                list_citation.append(cit)
                try:
                    author=citation.find('span',{'class':'auteurCitTxt'})
                    auteur=author_citation(author)

                    list_auteur.append(auteur.replace("-",""))
                
                except:
                    auteur="iconnu"
                    list_auteur.append(auteur)
                print("Citation : "+ cit +"\n"+ "Auteur : " + auteur.replace("-",""))
                try:
                    citf.write( 'Citation : ' + cit + '\n' + 'Auteur : ' + auteur.replace("-","") +'\n--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n' ) 
                except:
                    pass
j=len(list_citation)
i=0
if (len(list_auteur)==len(list_citation)):
    print(" succes \n")
with open("citations.csv", "w", newline='', encoding="utf-8") as fichier:
    writer=csv.writer(fichier)
    while i<j:
        try:
            writer.writerow((list_auteur[i],list_citation[i]))
            i+=1
        except:
                i+=1
        

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()

url = 'https://wvv.voirfilms.club/film-en-streaming'
r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, 'lxml')

print(soup)
url = "https://www.iziway.cm/search?q=veste"

reponse  = requests.get(url)

soups=BeautifulSoup(reponse.text,'lxml')
'''
soup=soup.find_all('div',{'class':'col-xl-3 col-lg-4 col-md-4 col-sm-6 col-6 '})
soup=soup.find_all('div',{'class':'ps-product  product-item'})
soup=soup.find_all('div',{'class':'ps-product__container'})
'''
soups=soups.find_all('div',{'class':'ps-product__content'})
for soup in soups:
    text=soup.find('a').text
    link=soup.find('a').get('href')
    prix=soup.find('p').text.replace(" ","")
    print("----> text :" + text + " | link : " + link + "| prix : " +  prix )