#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import read, write
import tweepy
import time
import random
import csv

#arquivos usados
#credencial API tweet
APIFILE='apikeys.txt'

#arquivo com ultima id visualizada
LASTSEEN = 'last_seen.txt'

#matriz de argumentos
MATRIX='matriz.csv'

#le arquivo de segredos da api
apikeys=open(APIFILE, 'r')
lines=apikeys.readlines()

api_key = lines[0].replace('\n', '')
api_secret_key = lines[1].replace('\n', '')
acess_key = lines[2].replace('\n', '')
acess_secret = lines[3].replace('\n', '')

apikeys.close()

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def read_last_seen(LASTSEEN):
    file_read = open(LASTSEEN, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(LASTSEEN, last_seen_id):
    file_write = open(LASTSEEN, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def random_phrase():
	frase=''
	#abre matrix e gera frase!
	with open(MATRIX, 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		for row in csv_reader:
			lenght=len(row)
			a=random.choice(range(lenght))
			frase=frase+row[a]+' '			
	csv_file.close()
	return frase 


def _main_():
    read_last_seen_str = str(read_last_seen(LASTSEEN))
    tweets = api.mentions_timeline(read_last_seen(LASTSEEN), tweet_mode = 'extended')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(LASTSEEN, tweet.id)
        genius_phrase = random_phrase()
        api.update_status('@'+ tweet.user.screen_name + ' ' + genius_phrase.decode('utf-8'), in_reply_to_status_id=tweet.id)

while True:
    _main_()
    time.sleep(60)
