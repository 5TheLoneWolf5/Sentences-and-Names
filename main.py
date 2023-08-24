def howManyNames(sentence):
  
  sentence = sentence.split(" ")

  for word in sentence:
    # for letter in word:
    word.strip()
    
  # Null value needs to be filtered after stripping whitespace.
  
  sentence = list(filter(None, sentence))

  # print(sentence, " TEST")
  
  count = 0
  
  for i in sentence:

    # print(i.split()[0][0])
    if i.split()[0][0].isupper():
      count += 1

  return count

def howManySentences(sentences):

  # Setting/stamping "." as the one to split the content.
  
  sentences = sentences.replace("?", ".")
  sentences = sentences.replace("!", ".")
  sentences = sentences.split(".")
  sentences = list(filter(None, sentences))

  numOfNames = []

  for sentence in sentences:
    numOfNames.append(howManyNames(sentence))

  return numOfNames

while True:
  
  sentenceInput = input("Entrada: ")
  
  for i in howManySentences(sentenceInput):
    print(i)