#!/usr/bin/python

import sys, socket, string, re, random, subprocess, ssl

HOST="iss.cat.pdx.edu"
PORT=6697
NICK="CombsBot"
IDENT="CombsBot"
REALNAME="Whopper's Bot"
CHAN="#catacombs"
readbuffer=""

#Random Variables _________________________________________
SerErrorCheck = 0
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s = ssl.wrap_socket(s,
                  cert_reqs=ssl.CERT_NONE,
                  do_handshake_on_connect=True)

s.connect((HOST, PORT))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))

s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.send("JOIN %s :%s\r\n" % (CHAN, "#######"))
# _________________________________________________________

while 1:
  readbuffer=readbuffer+s.recv(4096)
  temp=string.split(readbuffer, "\n")
  readbuffer=temp.pop( )

  for line in temp:
    line=string.rstrip(line)
    line=string.split(line)
    print line

# Lengthtemp is used throughout the script, mainly to check to syntax errors in input
    lengthtemp = len(line)
    if lengthtemp >= 4: # only parse lines if there are at least 3 words
# _______________________________OPTIONS ________________________________________
      if line[3] == ':!help':
        s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Options: !host $host/IP, !purpose $host/IP, !hardware $host/IP, !os $host/IP"))





# Keeps bot alive 
    if(line[0]=="PING"):
      s.send("PONG %s\r\n" % line[1])


if __name__ == '__main__':
  main()

