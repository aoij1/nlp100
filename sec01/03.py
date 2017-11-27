import re

sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
sentence = re.sub(re.compile("[!-/:-@[-`{-~]"), '', sentence)
word_list = sentence.split(' ')

word_dict = {}
for i, word in enumerate(word_list):
    if i==0 or i==4 or i==5 or i==6 or i==7 or i==8 or i==14 or i==15 or i==18: 
        key = word[0]
        word_dict[key] = 1 
    else:
        key = word[0]+word[1] 
        word_dict[key] = 2 
print(word_dict)
