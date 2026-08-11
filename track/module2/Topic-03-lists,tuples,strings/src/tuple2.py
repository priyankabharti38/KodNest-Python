# take input from user
sentence=input("Enter Senetnce: ")
word_position=int(input("Enter Word Position: "))
#remove space and convert to lower case
sentence=sentence.strip().lower()

#remove punctuation
punctuation=",.?!:;"
for p in punctuation:
    sentence=sentence.replace(p," ")

#split(),join() and len()method
words=sentence.split()
cleaned_sentence=" ".join(words)
print("Cleaned Sentence:",cleaned_sentence)
words_count=len(words)
print("Word Count:",words_count)

#print first and last word
first_word=words[0]
print("First Word:",first_word)
last_word=words[-1]
print("Last Word:",last_word)

#print first three char of first and last word
first_three_char=first_word[:3]
print("First Three Char:",first_three_char)
last_three_char=last_word[-3:]
print("Last Three Char:",last_three_char)

#print selected word
selected_word=words[word_position-1]
print("Selected Word:",selected_word)

