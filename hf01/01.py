sentence = input('sentence: ')
for word in sentence.split(' '):
  print(word[::-1], end=' ')
print()
