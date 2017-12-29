#!/usr/bin/python

import os
import glob
import time


def textReplace(filename, oldStr, newStr):
	fileData=""
	bakData=""
	bakname=filename+".bak"
	
	with open(filename, "r") as f:

		for line in f:
			bakData+=line
			if oldStr in line:
				line=line.replace(oldStr, newStr)
			fileData+=line

	with open(filename, "w") as f:
		f.write(fileData)
	with open(bakname, "w") as f:
		f.write(bakData)



def replaceAll(path, filename, oldStr, newStr):

	# for app
	# path=r"/home/rhome/app/"
	# filename="lib.defs"
	# oldStr=r"/home/app"
	# newStr=r"/home/rhome/app"

	target = path + r"*/"+filename	
	allFiles=glob.glob(target)

	for iFile in allFiles:
		
		textReplace(iFile, oldStr, newStr)


def gci(filepath):

	global N
	global path
	global filename
	global oldStr170
	global newStr

	files=os.listdir(filepath)
	for fi in files:
		if fi[0]==".":
			continue
		fi_d=os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		elif  fi==filename :
			N+=1
			#textReplace(fi_d, oldStr, newStr)
		

def allData(path):
	for root, dirs, files in os.walk(path, False):
		for name in files:
			print(os.path.join(root, name))
		for name in dirs:
			print(os.path.join(root, name))


def pathLevel1(filepath):
	files=os.listdir(filepath)
	for fi in files:
		if fi[0]==".":
			continue
		fi_d=os.path.join(filepath, fi)
		if os.path.isdir(fi_d):
			print(fi_d)			
			gci(fi_d)

########################

## global var
N=0
path=r"/home/rhome/app/"
filename="lib.defs"
oldStr=r"/home/app"
newStr=r"/home/rhome/app"


if __name__ == '__main__':
	
	print("path: "+path)
	print("file: "+filename)
	print("oldS: "+oldStr)
	print("newS: "+newStr)	

	start = time.time()
	files=pathLevel1(path)
	
	end = time.time()
	print("time: %f"%(end-start)) 
	print("total result: %d"%N)


