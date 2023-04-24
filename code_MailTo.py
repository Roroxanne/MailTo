import requests
import urllib.request #permettent de faire des requetes
from bs4 import BeautifulSoup #rendre pages accessibles
import pandas as pd #pour mettre l'objet dans un table
from selenium import webdriver #permettra de tansformer le 
#code dans "inspecter de la page en html"
from time import sleep #repos 

url = "https://mail.google.com/mail/u/0/?hl=fr#sent"
css_selector = ".zA yO" #id de la ligne du tableau avec l'adresse mail

wd_path = "PROJET ER/chromedriver" #chromedriver: pouvoir interagir avec la page google

wdriver = webdriver.Chrome(executable_path = wd_path) 

wdriver.get(url) #acceder à la page
sleep(4) #


