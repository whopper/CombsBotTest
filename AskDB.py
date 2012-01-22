#!/usr/bin/python

import sys, socket, string, re, subprocess, _mysql 
import MySQLdb

def main ():
#  subprocess.call(['echo "host test: hostname- test, IP- test, purpose- test OS - test" > queryresult'], shell=True)

  db=MySQLdb.Connection(host="localhost",user="whopper",
                        passwd="l33tk1tt3h",db="combs_vlan_noobz")

  cursor = db.cursor()

  linefile = open("/home/whopper/CombsBot/queryresult")
  toquery = []
  linetemp = []
  linetemp = linefile.readlines() 
  for lines in linetemp:  
    toquery.append(lines.rstrip('\r\n')) 

  cursor.execute("SELECT * FROM box WHERE ip_address = '%s'" % toquery[0])


  data = cursor.fetchall() 
  for each in data:
    print each

  subprocess.call(['echo "%s" > queryresult' % data], shell=True)

if __name__ == '__main__':
  main()

