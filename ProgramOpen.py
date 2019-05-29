# Program Opener

import subprocess
import os
from os import system
system("title Open Programs/Macros")

#loop = False

spotifylink = r'C:\Users\matth\AppData\Roaming\Spotify\Spotify.exe'
wordlink = r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
atomlink = r'C:\Users\matth\AppData\Local\atom\atom.exe'
chromelink = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
steamlink = r'C:\Program Files (x86)\Steam\Steam.exe'


print('What would you like to open?')
print('Programs: spotify, chrome, steam, word')
print('Macros: coding, write, TBH, TBH')
ProgramToOpen = input(">>> ")


if ProgramToOpen == "spotify":
    subprocess.Popen(spotifylink)
elif ProgramToOpen == "word":
    subprocess.Popen(wordlink)


#Macro 1 - CODING
if ProgramToOpen == "coding":
    subprocess.Popen(r'C:\Users\matth\Desktop\Programing\Python\Projects')
    #os.startfile(atomlink)

#Macro 2 - WRITE
if ProgramToOpen == "write":
    subprocess.Popen(wordlink)
    subprocess.Popen(spotifylink)
