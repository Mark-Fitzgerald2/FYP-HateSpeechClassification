
phrases = [["click this link", "dodgy"], ["weight drugs link", "dodgy"],["good drugs news", "dodgy"], ["kitten sleeping today", "fine"],["good luck kitten", "fine"],["smells good", "fine"],["tiger smells daisies", "fine"],["tiger link", "fine"]]

uniqueWords = []
fineWords = []
fineWordsCount = []
dodgyWords = []
dodgyWordsCount = []
positiveLabel = "fine"
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

probDodgy = dodgyPhrases / len(phrases)
probFine = finePhrases / len(phrases)

phraseToCheck1 = "good drugs link"
phraseToCheck2 = "sleeping drugs"

M1 = phraseToCheck1.split()
probMDodgy = probDodgy
probMFine = probFine
for w in M1:
	if w in dodgyWords:
		index = dodgyWords.index(w)
		count = dodgyWordsCount[index]
		probMDodgy *= count / sum(dodgyWordsCount)
	else:
		probMDodgy = 0
	if w in fineWords:
		index = fineWords.index(w)
		count = fineWordsCount[index]
		probMFine *= count / sum(fineWordsCount)
	else:
		probMFine = 0

probSum = probMDodgy + probMFine
actProbFine = probMFine / probSum
actProbDodgy = probMDodgy / probSum

if actProbFine > actProbDodgy:
	print("Fine")
	print(actProbFine)
else: 
	print("Dodgy")
	print(actProbDodgy)

print(uniqueWords)
print(fineWords)
print(fineWordsCount)
print(dodgyWords)
print(dodgyWordsCount)