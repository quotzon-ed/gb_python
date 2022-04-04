def f_up(sentence):
  sentence = sentence.split()
  res = ''
  for word in sentence:
    for letter in word:
      if ord(letter) < 97 or ord(letter) > 122:
        word = ''
        break
      else:
        word = word
    if word != '':
      res += word.title() + ' '
  return res

user_sentence = input("Enter some words: ")
print(f_up(user_sentence))