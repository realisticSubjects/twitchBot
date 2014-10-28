import socket

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



while True:
  irc_msg = irc.recv(1024) # receive data from the server
  irc_sender = irc_msg.split(':')[1]
  irc_sender = irc_sender.split('!')[0]
  print(irc_msg) # Here we print what's coming from the server
  print(irc_sender)

  if irc_msg.find('!hi') != -1:
    hello(irc_sender)
  if irc_msg.find('!ping') != -1: 
    irc.send(irc_msg.replace('!ping', 'pong'))
  if irc_msg.find('!cmd') != -1:
  	cmd()