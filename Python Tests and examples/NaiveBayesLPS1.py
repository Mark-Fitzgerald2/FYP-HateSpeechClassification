
phrases = [["lol coming from a nigger Where's the kkk when you need them.", "hate"], ["Can you not read nigger Nobody's touching The Slaughter King", "hate"],["Pretty sure your the nigger bashing idiot , defending the white cops when it was clearly murder but whatever bitch", "hate"], ["You are a racist.  Black entertainers use the word nigger more than anyone.  You can't pretend to be offended by a word that you use", "hate"],["We can not lead an organization, we can run an organization. We can only lead people.", "Non hate"],["Thank you to everyone who bought Leaders Eat Last. Because of you, the book is now a New York Times Bestseller.", "Non hate"],["Great companies don't cheer at others' losses or cry at their wins. Instead, they focus on their own work...which is what makes them great.", "Non hate"],["Is \"thank you\" the new \"sorry\"? Research shows woman apologize more than men.", "Non hate"]]

uniqueWords = []
fineWords = []
fineWordsCount = []
dodgyWords = []
dodgyWordsCount = []
positiveLabel = "Non hate"
dodgyPhrases = 0
finePhrases = 0

for phrase in phrases:
	words = phrase[0].split()
	if phrase[1] == positiveLabel:
		finePhrases += 1
	else:
		dodgyPhrases += 1
	for word in words:
		if word not in uniqueWords:
			uniqueWords.append(word)
		if phrase[1] == positiveLabel:
			
			if word not in fineWords:
				fineWords.append(word)
				fineWordsCount.append(1)
			else: 
				index = fineWords.index(word)
				fineWordsCount[index] += 1
		else:
			
			if word not in dodgyWords:
				dodgyWords.append(word)
				dodgyWordsCount.append(1)
			else: 
				index = dodgyWords.index(word)
				dodgyWordsCount[index] += 1

probDodgy = (dodgyPhrases + 1) / (len(phrases) + 2)
probFine = (finePhrases + 1) / (len(phrases) + 2)

phraseToCheck1 = "good drugs link"
phraseToCheck2 = "nigger"

M1 = phraseToCheck2.split()
probMDodgy = probDodgy
probMFine = probFine
for w in M1:
	if w in dodgyWords:
		index = dodgyWords.index(w)
		count = dodgyWordsCount[index]
		probMDodgy *= (count + 1) / (sum(dodgyWordsCount) + len(uniqueWords))
	else:
		probMDodgy *= 1 / (sum(dodgyWordsCount) + len(uniqueWords))
	if w in fineWords:
		index = fineWords.index(w)
		count = fineWordsCount[index]
		probMFine *= (count + 1) / (sum(fineWordsCount) + len(uniqueWords))
	else:
		probMFine *= 1 / (sum(fineWordsCount) + len(uniqueWords))

probSum = probMDodgy + probMFine
actProbFine = probMFine / probSum
actProbDodgy = probMDodgy / probSum

if actProbFine > actProbDodgy:
	print("Non Hate")
	print(actProbFine)
else: 
	print("Hate")
	print(actProbDodgy)


print(len(uniqueWords))
