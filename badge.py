import config
import urllib3
import json
from authentication import Authentication
import pygame
import threading
from datetime import datetime
import time
import os
import sys

gray = (30,30,30)
white = (255,255,255)
res = (720,720)

StateOfCardReader = 0 # 0 Wait a card, 1 Card is valid, 2 card is not valide, 3 sent old log
AuthError = ""
WindowIsOpen = True

textShell=""
SendOldLog = False
MomentOfNonSent = 0
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cmd = "nfc-poll|grep UID"

pygame.display.set_caption("Badgeuse")
Window = pygame.display.set_mode(res)
tuxImage = pygame.image.load("tux.png")
DLImage = pygame.image.load("download.png")
AcceptImage = pygame.image.load("accept.png")
NotAcceptImage = pygame.image.load("negative.png")

Window.fill(gray)

def writeToFile(rfid):
	date = datetime.now()
	FileToWrite = open("HistoryOfPassage.log",mode="a")
	FileToWrite.writelines(rfid+","+str(date)+"\n")
	FileToWrite.close()

pygame.display.flip()

while WindowIsOpen:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			WindowIsOpen = False
	AuthError=""
	StateOfCardReader=0
	Window.fill(gray)
	Window.blit(tuxImage,[10,10])
	pygame.display.flip()
	textShell = os.popen(cmd).read().strip()
	#Read the card
	if (textShell.startswith("UID")):
		UIDWithSpace = textShell.split(":")[1]
		UIDWithoutSpace = UIDWithSpace.replace("  ",":").strip()
		print(UIDWithoutSpace)
		try:
			auth = Authentication(rfid=UIDWithoutSpace)
			auth.add_passage_to_log()
		except KeyError:
			StateOfCardReader = 2
		except :
			AuthError = "Attention le serveur est innacesible sauvegarde des passages en local"
			StateOfCardReader = 1
			SendOldLog = True
			MomentOfNonSent = time.time()
			writeToFile(UIDWithoutSpace)
	
	# Send the oldlog if the Dokos Server had problem
	if SendOldLog and (time.time()-MomentOfNonSent>60):
		Window.fill(gray)
		Window.blit(DLImage,[10,10])
		pygame.display.flip()
		FileToRead = open("HistoryOfPassage.log",mode="r")
		OldLogString = FileToRead.read()
		FileToRead.close()
		os.remove("HistoryOfPassage.log")
		OldLogList = OldLogString.split("\n")
		OldLogList.pop()
		print(OldLogList)
		StateOfCardReader = 3
		AuthError = "Envoie des données locales au serveur"
		SendOldLog = False
		for e in OldLogList:
			try:
				auth = Authentication(rfid=e.split(',')[0])
				auth.add_passage_to_log(date=e.split(',')[1])
			except KeyError:
				pass
			except:
				SendOldLog = True
				MomentOfNonSent = time.time()
				FileToWrite = open("HistoryOfPassage.log",mode="a")
				FileToWrite.writelines(e.split(',')[0]+","+e.split(',')[1]+"\n")
				FileToWrite.close()

	print(AuthError,StateOfCardReader)
	Window.fill(gray)
	if StateOfCardReader==1:
		Window.blit(AcceptImage,[10,10])
	elif StateOfCardReader==2:
		Window.blit(NotAcceptImage,[10,10])
	else:
		Window.blit(tuxImage,[10,10])
	pygame.display.flip()
	time.sleep(3)
