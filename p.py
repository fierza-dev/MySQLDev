K='[ >_< ] Good Bye....';J=False;I='cli';C=exit;A=print
import aiohttp as L,asyncio as M,time as B,os,random as N,sys
from os import system as G,name
from zipfile import ZipFile as O
from InquirerPy import prompt as P,inquirer as D
def E(s):
	for A in s+'\n':sys.stdout.write(A);sys.stdout.flush();B.sleep(N.random()*.4)
async def Q(url,dirname):
	D=dirname
	async with L.ClientSession()as H:
		async with H.get(url)as F:
			if F.status==200:
				G=os.path.join(D,'MySQLDev(CLI).zip');E('Downloading files...');B.sleep(1)
				with open(G,'wb')as I:I.write(await F.read())
				A('Download & Save File Successfully...');B.sleep(1);E('Extracting files...');B.sleep(1)
				with O(G,'r')as J:J.extractall(D)
				A('File extraction was successful...');B.sleep(1);A('Download & Extract File Complete...');A('\nHappy Hacking :)');C()
			else:A('[ ✕ ] Error....');C()
def R(url,download_type,dirname):
	if download_type==I:C=M.get_event_loop();C.run_until_complete(Q(url,dirname))
	else:A("You haven't selected a valid version.");B.sleep(2);F()
def S():
	F=D.confirm(message='Create New Directory??',default=J).execute();C=D.text(message='Enter your directory name: ').execute()
	if F:E('Create Directory...');os.mkdir(C);B.sleep(1);A('Create Directory was successful...');B.sleep(1)
	R('https://github.com/fierza-dev/fierza-dev.github.io/raw/main/MySQLDev(CLI).zip',I,C)
def T():S()
def U():
	I='Exit';H='All Version [ ✕ ]';G='CLI Version [ ✓ ]';F='Desktop Version [ ✕ ]';E='Web Version [ ✕ ]';B='menu';J=[{'type':'list','name':B,'message':'Menu : ','choices':[E,F,G,H,I]}];D=P(J)
	if D[B]==E:A(f"[ ! ] in development..");C()
	elif D[B]==F:A(f"[ ! ] in development..");C()
	elif D[B]==G:T()
	elif D[B]==H:A(f"[ ! ] in development..");C()
	elif D[B]==I:A(K);C()
def F():
	if os.name=='nt':G('cls')
	else:G('clear')
	A(""" 
 © 2023 FierzaDev™. All Rights Reserved.         
 ____    ____         ______    ___     _____    ______                 
|_   \  /   _|      .' ____ \ .'   `.  |_   _|  |_   _ `.               
  |   \/   |   _   _| (___ \_/  .-.  \   | |      | | `. \.---. _   __  
  | |\  /| |  [ \ [  _.____`.| |   | |   | |   _  | |  | / /__\[ \ [  ] 
 _| |_\/_| |_  \ '/ | \____) \  `-'  \_ _| |__/ |_| |_.' | \__.,\ \/ /  
|_____||_____[\_:  / \______.'`.___.\__|________|______.' '.__.' \__/  INSTALLER
              \__.'                  
   """);U()
if __name__=='__main__':
	try:F()
	except KeyboardInterrupt:
		H=True;H=D.confirm(message='Do you want to exit??',default=J).execute()
		if H:A(K);C()
		else:F()