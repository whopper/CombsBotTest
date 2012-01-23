#!/usr/bin/python

import sys, socket, string, re, subprocess, _mysql 
import MySQLdb

def main ():
#  subprocess.call(['echo "host test: hostname- test, IP- test, purpose- test OS - test" > queryresult'], shell=True)

  resultdisplay = "Results: Format: IP - Username - Hostname - OS - Purpose - Hardware"

  db=MySQLdb.Connection(host="localhost",user="whopper",
                        passwd="######",db="combs_vlan_noobz")


  linefile = open("/home/whopper/CombsBot/queryresult")
  toquery = []
  linetemp = []
  linetemp = linefile.readlines() 
  for lines in linetemp:  
    toquery.append(lines.rstrip('\r\n')) 

  cursor = db.cursor()

  # Args
  if  sys.argv[1] == 'host':
    testint = str(toquery)
    print testint[2]

    if testint[2] == '1':
      cursor.execute("SELECT * FROM box WHERE ip_address = '%s'" % toquery[0])
    else:
      cursor.execute("SELECT * FROM box WHERE boxname = '%s'" % toquery[0])

    data = cursor.fetchall() 
    strdata = str(data)
    print strdata[22:25]
    if strdata[22:25] == '\\n\'':
      subprocess.call(['echo "No host registered for IP %s" > queryresult' % toquery], shell=True)

    else:
      subprocess.call(['echo "%s" > queryresult' % resultdisplay], shell=True)
      subprocess.call(['echo "%s" >> queryresult' % data], shell=True)

  elif sys.argv[1] == 'owner':
    cursor.execute("SELECT * FROM box WHERE owner = '%s'" % toquery[0])

    data = cursor.fetchall()
    strdata = str(data)
    if strdata[2:3] == '\'\'':
      subprocess.call(['echo "No host registered for %s" > queryresult' % toquery], shell=True)

    else:
      subprocess.call(['echo "% s" > queryresult' %resultdisplay], shell=True)
      subprocess.call(['echo "%s" >> queryresult' % data], shell=True)


if __name__ == '__main__':
  main()

