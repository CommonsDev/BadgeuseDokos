# coding: utf-8
# Import all the library
import os # To open the files
from pathlib import Path
import shutil
import configFiles

def separeFileAndDir(path):
	"""

	"""
	files = []
	directory = []
	try :
		imageFiles = os.listdir(path)
	except:
		return files,directory
	for e in imageFiles:
		if os.path.isfile(path+e):
			files.append(e)
		elif os.path.isdir(path+e):
			directory.append(e)
	return files,directory

def deleteAllSearchFileInPath(path,stringsToSearch,rec=False):
	"""

	"""
	files,directories = separeFileAndDir(path)
	search_in_directory = False
	cmd = "ls -R | grep "
	textShell = ""
	if rec==True:
		i = 0
		j = 0
		while i<len(files):
			while j<len(stringsToSearch):
				if stringsToSearch[j] in files[i].lower():
					os.remove(path+files[i])
					print(path+files[i]," a été supprimé.")
					break
				j+=1
			j=0
			i+=1
		i = 0
		j = 0
		while i<len(directories):
			search_in_directory = False
			try:
				os.chdir(path+directories[i]+"/")
			except:
				break:
			while j<len(stringsToSearch):
				if stringsToSearch[j] in directories[i].lower():
					shutil.rmtree(path+directories[i])
					break
				textShell = os.popen(cmd+stringsToSearch[j])
				if textShell !="":
					search_in_directory=True
				j+=1
			j=0
			if search_in_directory==True:
				deleteAllSearchFileInPath(path+directories[i]+"/",stringsToSearch,rec)
			i+=1
	else:
		i = 0
		j = 0
		while i<len(files):
			while j<len(stringsToSearch):
				if stringsToSearch[j] in files[i].lower():
					os.remove(path+"/"+files[i])
					break
				j+=1
			j=0
			i+=1

deleteAllSearchFileInPath(configFiles.path,configFiles.stringsToSearch,configFiles.rec)