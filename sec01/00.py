word='stressed'
word_length=len(word)
word_reversed=''
for i in range(word_length):
  word_reversed += word[word_length-i-1]

print(word_reversed)
