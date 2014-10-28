import socket
import random
import pymongo

from pymongo import MongoClient
from bson.objectid import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['twitchBot']
collection = db['ronnaldmcdonald']
#posts = db.posts

bot_owner = 'ronnaldmcdonald'
botnick = 'burgerzkingbot' #Bot Name (Twitch.Tv Bot Name)
channel = '#ronnaldmcdonald' #Stream Channel (Twitch.Tv Stream)
server = 'irc.twitch.tv' #IRC Server (Server)
password = 'oauth:7g2y8p9fvka7xq0pex3gr7d5p3za0q' #Password (oAuth)


queue = 13
irc = socket.socket()
irc.connect((server, 6667))

irc.send('PASS ' + password + '\r\n')
irc.send('USER ' + botnick + ' 0 * :' + bot_owner + '\r\n')
irc.send('NICK ' + botnick + '\r\n')
irc.send('JOIN ' + channel + '\r\n')

def hello(irc_sender):
  	irc.send("PRIVMSG "+ channel +" :Hello " + irc_sender + ' !\n')

def cmd():
	irc.send("PRIVMSG "+ channel +" :!ping / !hi /!cmd\n")

def gessNumber(client, db, collection):
  print("in gess number")
  goal = str(18)#random.randint(1,20)
  gess = False
  while (gess == False):
    irc_msg = irc.recv(1024) # receive data from the server
    irc_sender = irc_msg.split(':')[1]
    irc_sender = irc_sender.split('!')[0]

    if irc_msg.find(goal) != -1:
      print("TRUE")
      #irc.send("GG")
      irc.send("PRIVMSG "+ channel + " :Victoire !! " + irc_sender + " gagne 10 pts!\n")
      
      print collection.find_one({'_id': ObjectId('544fdf11795c636402b521a0')})
      
      collection.update({'nick':"ronnaldmcdonald"}, {'$inc': {'points' : 10}})
      
      gess = True
      break


while True:
  irc_msg = irc.recv(1024) # receive data from the server
  irc_sender = irc_msg.split(':')[1]
  irc_sender = irc_sender.split('!')[0]
  print(irc_msg) # Here we print what's coming from the server
  
  if irc_msg.find('!hi') != -1:
    hello(irc_sender)
  if irc_msg.find('!ping') != -1: 
    irc.send(irc_msg.replace('!ping', 'pong'))
  if irc_msg.find('!cmd') != -1:
  	cmd()
  if irc_msg.find('!gess') != -1:
    gessNumber(client, db, collection)

