#27.5
with open('words_1.txt','r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count +=1
print(count)

#27.6
with open('words_2.txt', 'r') as file:
  a = file.readline()
  words=a.split()
  for word in words:
    if 'c' in word:
      print(word.strip(',.'))