
import random
from utils.instanciadorSelenium.Navegador import Abrir_navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    
reddit_url = config['reddit_url']
api_url = config['api_url']

posts = []



def acessar_reddit_br_dev():
    global driver
    driver.get(reddit_url)
    
    
def capturar_posts(driver):
    global posts
    posts = []
    while len(posts) < 60:
        posts = driver.find_elements(By.TAG_NAME, 'shreddit-post')
        posts[-1].location_once_scrolled_into_view
        sleep(random.randint(4,10))
    
    
def armazenar_no_banco(driver, posts):   
    #post = 2
    for post in posts:
        post.get_attribute('author')
        post.get_attribute('post-title')
        post.get_attribute('comment-count')
        post.get_attribute('content-href')
        
        if (int(post.get_attribute('comment-count')) > 9):
            print('é')
            conteudo = post.find_elements(By.TAG_NAME, 'p')
            len(conteudo)
        
            postConteudo = ''
            for texto in conteudo:
                if len(texto.text) > 1: 
                    if len(postConteudo) > 1:
                        postConteudo += '\n'
                    postConteudo += (texto.text)
        
            response = requests.post(api_url, json={
                'autor': post.get_attribute('author'),
                'titulo': post.get_attribute('post-title'),
                'quantidade_comentarios': int(post.get_attribute('comment-count')),
                'link_publicacao': post.get_attribute('content-href'),
                'conteudo': postConteudo
            })
            # response.status_code
            # response.text
        else:pass
        
        
while True:
    driver = Abrir_navegador()
    acessar_reddit_br_dev()
    capturar_posts(driver)
    armazenar_no_banco(driver, posts)
    driver.close()
    sleep(21600)
    



    