#!/usr/bin/python

import sys, socket, string, re, random, subprocess, ssl

def main():
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
          s.send("PRIVMSG %s :%s\r\n" % (CHAN, "Options: !host $host/IP - gives info about a Combs box"))

        if line[3] == ':!host' or '!host' in line:
          subprocess.call(['echo %s > queryresult' % line[4]], shell=True)
          subprocess.call(["/home/whopper/CombsBot/AskDB.py"], shell=True)
          FileWriter(s, CHAN)





  # Keeps bot alive 
      if(line[0]=="PING"):
        s.send("PONG %s\r\n" % line[1])

def FileWriter(s, CHAN): 
 
  tempfile = open("/home/whopper/CombsBot/queryresult")
  i = 0
  k = 0
  tlist1 = []
  tlist2 = []

  tlist2 = tempfile.readlines()
  tlist2length = len(tlist2)
  for each in tlist2:
    tlist1.append(each.rstrip('\r\n'))
    i = i + 1
  if i > 1:
    for each in tlist2:
      while k < tlist2length:
        s.send("PRIVMSG %s :%s\r\n" % (CHAN, "%s" % tlist2[k]))
        k = k + 1
  else:
    s.send("PRIVMSG %s :%s\r\n" % (CHAN, "%s" % tlist1[0]))

#  subprocess.call(['rm /home/whopper/CombsBot/queryresult'], shell=True)


if __name__ == '__main__':
  main()

