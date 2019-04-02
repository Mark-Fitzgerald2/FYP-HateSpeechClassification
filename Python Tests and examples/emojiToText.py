import emoji

#print(dir(emoji))
class emojiToText(object):

#text = "Hey Oisin, I am 😠"#"First, we established subjects. I was 🤓, and I could use it to represent “me” in sentences. For example, 🤓🏃‍🏢 could mean “I’m running to work. 😀 😁 😂 🤣 😃 😄"#emoji.emojize(':thumbs_up: :bowtie: :angry: :yum: :hushed: :sweat:')
#print(text)
#print(emoji.demojize(text))
	def demojize(self, text):
		return emoji.demojize(text)