import requests
import urllib.request
import lyricsgenius as genius
from bs4 import BeautifulSoup
import re
import random

"""
Input: A txt file of every drake song, with each song sepearated by FOUR new lines
Outputs: A sick Drake rap 
"""

def parseLyrics(lyrics):
    dict = {}
    dict[" NEWLINE\n"] = []
    # read every line of every drake song
    prevWord = ""
    newLineCount = 0
    for line in lyrics:
        # if character starts as new line 
        if line == '':
            newLineCount+=1
            # if there is four lines in a row map prev word to END_SONG
            if newLineCount == 4:
                if prevWord in dict:
                    dict[prevWord].append("END_SONG")
                else: 
                    dict[prevWord] = []
                    dict[prevWord].append("END_SONG")
                newLineCount = 0
                prevWord = "START_SONG"     
        elif line[0] == "[":
            #Delete all characters after and including :
            sep = ":"
            rest = line.split(sep, 1)[0]
            #Reappend ]
            rest += "]"
            #If prevWord is a word map map else if END_SONG do not map
            if prevWord not in ["END_SONG",""]:
                if prevWord in dict:
                    dict[prevWord].append(rest)
                else:
                    dict[prevWord] = []
                    dict[prevWord].append(rest)
            prevWord = rest
        else:
            #iterate for everyword in the line
            i = 0 
            for word in line.split():
                if prevWord in dict:
                    dict[prevWord].append(word)
                    prevWord = word
                else:
                    dict[prevWord] = []
                    dict[prevWord].append(word)
                if i == 0:
                    dict[" NEWLINE\n"].append(word)
                i+=1
                prevWord = word
            if prevWord in dict:
                    dict[prevWord].append(" NEWLINE\n")
                    prevWord = word
            else:
                dict[prevWord] = []
                dict[prevWord].append(" NEWLINE\n")
            # if first word in line \n -> maps to word
            # if last word in line: word -> \n
            # else prevWord -> word 
    return dict

def drakeversal(dictonary):
    song = ""
    current = random.choice(dictonary["START_SONG"])
    while current != "END_SONG":
        song+= " " + current
        current = random.choice(dictonary[current])
    return song
# Read in textfile 
lyricsFile = open("Lyrics_Drake.txt","r")
lyricsTxt = lyricsFile.readlines()
lyricsTxt = [line.strip() for line in lyricsTxt]
draktionary = parseLyrics(lyricsTxt)
print(drakeversal(draktionary))
# Parse textfile by each song 
# Create markov model 
# Create new song

