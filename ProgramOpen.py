# Program/macro Opener
#Matthew Christie
#May 2019

#Notes:
#subprocess.Popen works for programs
#os.startfile opens a dir or file within the os

import subprocess
import os
from os import system
system("title Open Programs/Macros")

#List of program locations              (Create an array??)
spotifylink = r'C:\Users\matth\AppData\Roaming\Spotify\Spotify.exe'
wordlink = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
atomlink = r'C:\Users\matth\AppData\Local\atom\atom.exe'
chromelink = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
steamlink = r'C:\Program Files (x86)\Steam\Steam.exe'

#Prompt for Input
print('What would you like to open?')
print('Programs: spotify, chrome, steam, word')
print('Macros: coding, write, TBA, TBA')
ProgramToOpen = input(">>> ")

#Basic Program Openers
if ProgramToOpen == "spotify":
    subprocess.Popen(spotifylink)
elif ProgramToOpen == "word":
    subprocess.Popen(wordlink)
elif ProgramToOpen == "steam"
    subprocess.Popen(steamlink)
elif ProgramToOpen == "chrome"
    subprocess.Popen(chromelink)


#Macro 1 - CODING
if ProgramToOpen == "coding":
    os.startfile(r'C:\Users\matth\Desktop\Programing\Python\Projects')
    subprocess.Popen(atomlink)

#Macro 2 - WRITE
if ProgramToOpen == "write":
    subprocess.Popen(wordlink)
    subprocess.Popen(spotifylink)
