#!/usr/bin/env python3

"""
VocTrainer
Copyright (C) 2016 LNJ <git@lnj.li>
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from random import randint

CREATE_NEW_DICT = -1

class Entry:
	def __init__(self, word1, word2):
		self.word1 = word1
		self.word2 = word2

class Dictionary:
	def __init__(self, name, langName1, langName2):
		self.name = name
		self.langName1 = langName1
		self.langName2 = langName2
		self.vocList = [Entry("hello", "Hallo")]
		self.statsAsked = 0
		self.statsWrong = 0
		self.statsTrue = 0
	def addEntry(self, word1, word2):
		self.vocList.append(Entry(word1, word2))
	def addEntryUI(self):
		while True:
			word1 = input("Please enter a word in " + self.langName1 + ": ")
			if word1 == "#": return
			word2 = input("Please enter a word in " + self.langName2 + ": ")
			if word2 == "#": return
			correct = input("Is this correct? [Y/n] ")
			if correct == "#": return
			while not (correct == "" or correct == "y" or correct == "Y"):
				word1 = input("Please enter a word in " + self.langName1 + ": ")
				if word1 == "#": return
				word2 = input("Please enter a word in " + self.langName2 + ": ")
				if word2 == "#": return
				correct = input("Is this correct? [Y/n] ")
				if correct == "#": return
			self.addEntry(word1, word2)
			print("Added ["+ word1 + ", " + word2 + "] to " + self.name + ".")

	def checkVoc(self):
		while True:
			entry = self.vocList[randint(0, len(self.vocList) - 1)]
			answer = input("Translation to " + self.langName2 + " from " +
				entry.word2 + ": ")
			if answer == entry.word1:
				print("That's true! Nice one.")
			elif answer == "#":
				break
			else:
				print("Wrong! Right answer was: " + entry.word1)

class Library:
	def __init__(self):
		self.dicts = {}
	def addDict(self, name, langName1, langName2):
		self.dicts[name] = Dictionary(name, langName1, langName2)
	def printDicts(self, printNums = False, printNewDict = False):
		print("List of Dictionaries:")
		i = 0
		for dictName in self.dicts.keys():
			i += 1
			Dict = self.dicts[dictName]
			number = ""
			if printNums:
				number = "[" + str(i) + "] "
			print(number + Dict.langName1 + "-" + Dict.langName2 +
				" - " + Dict.name)
		# print an option to create a new Dictionary
		if printNewDict:
			if printNums:
				print("[" + str(i+1) + "] Create a new Dictionary ...")
			else:
				print("Add a new Dictionary ...")

	def checkNumber(self, number, compare):
		try:
			number = int(number)
			if number >= 1 and number <=  compare:
				return True
		except: pass
		return False

	def selectDictUI(self, allowNewDict = False):
		self.printDicts(printNums = True, printNewDict = allowNewDict)
		maxDict = len(self.dicts)
		maxPossibleInput = len(self.dicts)
		if allowNewDict: maxPossibleInput += 1

		text = ("Which Dictionary do you want to use? [1-" +
			str(maxPossibleInput) + "] ")
		dictId = input(text)
		# repeat until the given string is valid
		while not self.checkNumber(dictId, maxPossibleInput):
			dictId = input(text)
		dictId = int(dictId)

		if not allowNewDict or dictId <= maxDict:
			return list(self.dicts.keys())[dictId-1] # return the name of dictId
		else:
			return CREATE_NEW_DICT

	def checkVocUI(self):
		dictName = self.selectDictUI()
		if dictName:
			self.dicts[dictName].checkVoc()

	def addDictUI(self):
		newName = input("Please enter a new name: ")
		lang1 = input("Please enter the first language: ")
		lang2 = input("Please enter the second language: ")
		correct = input("Is this correct? [Y/n] ")
		while not (correct == "" or correct == "y" or correct == "Y"):
			newName = input("Please enter a new name: ")
			lang1 = input("Please enter the first language: ")
			lang2 = input("Please enter the second language: ")
			correct = input("Is this correct? [Y/n] ")

		self.addDict(newName, lang1, lang2)
		return newName

	def addEntryUI(self):
		dictName = self.selectDictUI(allowNewDict = True)
		if dictName == CREATE_NEW_DICT:
			dictName = self.addDictUI()
		self.dicts[dictName].addEntryUI()





baseLib = Library()
baseLib.addDict("English G 21 - D5 - Unit 1", "English", "German")

def main():
	print("Availiable Commands:")
	print("addentry, adddict, checkvoc, exit, help")
	while True:
		befehl = input("$ ")
		if befehl == "addentry":
			baseLib.addEntryUI()
		elif befehl == "adddict":
			baseLib.addDictUI();
		elif befehl == "checkvoc":
			baseLib.checkVocUI()
		elif befehl == "help":
			print("Availiable Commands:")
			print("addentry, adddict, checkvoc, exit, help")
		elif befehl == "exit":
			break
		else:
			print("That's not a valid command, sorry. Type 'help'" +
				" for a list of commands")
	print("Not saving.")



if __name__ == "__main__":
	main()
