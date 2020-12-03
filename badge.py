import config
import urllib3
import json
from authentication import Authentication
import tkinter as Tk
import threading
from pathlib import Path
from datetime import datetime
import time
import os
import sys
from PIL import Image,ImageTk


WindowOpen = True
StateOfCardReader = 0 # 0 Wait a card, 1 Card is valid, 2 card is not valide, 3 reader is currenty not available, 4 sent old log
AuthError = ""


class ReadCard(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run():
		global WindowOpen
		global StateOfCardReader
		global AuthError
		FileToWrite = None
		textShell=""
		SendOldLog = False
		MomentOfNonSent = 0
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
		cmd = "nfc-poll|grep UID"
		while WindowOpen:
			StateOfCardReader=0
			AuthError = ""
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
				except ConnectionError :
					AuthError = "Attention le serveur est innacesible sauvegarde des passages en local"
					StateOfCardReader = 1
					SendOldLog = True
					MomentOfNonSent = time.time()
					date = datetime.now()
					FileToWrite = open("HistoryOfPassage.log",mode="a")
					FileToWrite.writelines(UIDWithoutSpace+","+str(date)+"\n")
					FileToWrite.close()
				except :
					AuthError = "Unexpected error:" +sys.exc_info()[0]
					StateOfCardReader = 2
			elif ("ERROR" in textShell):
				StateOfCardReader = 3
			else:
				StateOfCardReader = 2
			# Send the oldlog if the Dokos Server had problem
			if SendOldLog and (time.time()-MomentOfNonSent<60):
				FileToRead = open("HistoryOfPassage.log",mode="r")
				OldLogString = FileToRead.read()
				FileToRead.close()
				os.remove("HistoryOfPassage.log")
				OldLogList = OldLogString.split("\n")
				StateOfCardReader = 4
				AuthError = "Envoie des données locales au serveur"
				for e in OldLogList:
					try:
						auth = Authentication(rfid=e.split(",")[0])
						auth.add_passage_to_log(date=e.split(",")[1])
					except ConnectionError:
						SendOldLog = True
						MomentOfNonSent = time.time()
						FileToWrite = open("HistoryOfPassage.log",mode="a")
						FileToWrite.writelines(e.split(",")[0]+","+e.split(",")[1]+"\n")
						FileToWrite.close()
			time.sleep(2)


class GUI(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run():
		global WindowOpen
		global StateOfCardReader
		global AuthError
		Window = Tk.Tk(screenName="NFC Reader")
		Window.config(background="#181818")
		nom_fichier = ""
		#Print the state of the reader (waiting, valide card or not valide card)
		if StateOfCardReader==0:
			nom_fichier="tux.png"
		elif StateOfCardReader==1:
			nom_fichier="accept.png"
		elif StateOfCardReader==2:
			nom_fichier="negative.png"
		elif StateOfCardReader==3:
			nom_fichier="usb.png"
		else:
		nom_fichier="download.png"
		LoadImage = Image.open(nom_fichier)
		LoadImageTk = ImageTk.PhotoImage(LoadImage)
		PhotoCanva = tk.Canvas(Window,width=640,height=640,bg="#181818")
		PhotoCanva.create_image(640/2,640/2,image=LoadImageTk)
		PhotoCanva.pack()
		ErrorLabel = tk.Label(Window,text=AuthError,bg="#181818",fg="white")
		ErrorLabel.pack()
		Window.mainloop()
		WindowOpen=False

ReadingCard = ReadCard()
TkWindow = GUI()

TkWindow.start()
ReadingCard.start()

TkWindow.join()
ReadingCard.join()