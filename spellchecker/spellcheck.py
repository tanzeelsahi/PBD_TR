

words = open("spell.words").readlines()
words = map(lambda x: x.strip(), words)

# print words
print len(words)
print words[0]
print words[len(words)-1]

print('zygotic' in words)
print('mistasdas' in words)

def load_words(file_name):
    words = open(file_name).readlines()
    words = map(lambda x: x.strip(), words)
    return words

print load_words("spell.words")[0]

def load_file(self, file_name):
    lines = open(file_name).readlines()
    lines = map(lambda x: x.strip().lower(), lines)
    return lines

def check_word(words, word):
    return word in words

	
def check_words(words, sentence):
	words_to_check = sentence.split(' ')
	failed_words = []
	for word in words_to_check:
		if not check_word(words, word):
			print('Word is misspelt : ' + word)
			failedwords.append(word)
		return failedwords
	
def checkdocument(self, file_name):
	self.sentences = self.load_file(file_name)
	failed_words_in_sentences = []
	index = 0
	for sentence in self.sentences:
		failed_words_in_sentences.extend(self.check_words(sentence))
		index = index + 1
	return failed_words_in_sentences


		

