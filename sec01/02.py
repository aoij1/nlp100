import re

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sentence = re.sub(re.compile("[!-/:-@[-`{-~]"), '', sentence)
word_list = sentence.split(' ')
word_cnt_list = []

for w in word_list:
  word_cnt_list.append(len(w))

print(word_cnt_list)
