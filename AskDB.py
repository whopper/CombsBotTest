#!/usr/bin/python

import sys, socket, string, re, subprocess, _mysql 
import MySQLdb

def main ():
#  subprocess.call(['echo "host test: hostname- test, IP- test, purpose- test OS - test" > queryresult'], shell=True)

  db=MySQLdb.Connection(host="localhost",user="whopper",
                        passwd="#######",db="combs_vlan_noobz")


  linefile = open("/home/whopper/CombsBot/queryresult")
  toquery = []
  linetemp = []
  linetemp = linefile.readlines() 
  for lines in linetemp:  
    toquery.append(lines.rstrip('\r\n')) 

  cursor = db.cursor()
  cursor.execute("SELECT * FROM box WHERE ip_address = '%s'" % toquery[0])

  data = cursor.fetchall() 
  strdata = str(data)
  print strdata[22:25]
  print ":ALALALA"
  if strdata[22:25] == '\\n\'':
    subprocess.call(['echo "No host registered for IP %s" > queryresult' % toquery], shell=True)

  else:
    subprocess.call(['echo "Results: Format: IP - Username - Hostname - OS - Purpose - Hardware" > queryresult'], shell=True)
    subprocess.call(['echo "%s" >> queryresult' % data], shell=True)


if __name__ == '__main__':
  main()

