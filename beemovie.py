import requests
import random
import sys

def getScript():
  r = requests.get('https://gist.githubusercontent.com/The5heepDev/a15539b297a7862af4f12ce07fee6bb7/raw/7164813a9b8d0a3b2dcffd5b80005f1967887475/entire_bee_movie_script')
  return r.text
  
def getKey(text):
  text = text.split(' ')
  return list(set(text))

def occurrenceMatrix(key, text):
    text = text.split(' ')
    matrix = [[0 for i in range(len(key))] for i in range(len(key))]
    for word in key:
      wordIndex = key.index(word)
      locations = [i for i,x in enumerate(text) if x == word]
      for i in locations:
        if i != len(text)-1:
          nextWord = text[i+1]
          nextWordIndex = key.index(nextWord)
          matrix[wordIndex][nextWordIndex] = matrix[wordIndex][nextWordIndex] + 1
    return matrix

def probabilityMatrix(matrix):
    for lineIndex in range(len(matrix)):
      if sum(matrix[lineIndex]) != 0:
        matrix[lineIndex] = list(map(lambda x: x/sum(matrix[lineIndex]), matrix[lineIndex]))
    return matrix

def checkProbability(matrix, key, word1, word2):
    word1Index = key.index(word1)
    word2Index = key.index(word2)
    return matrix[word1Index][word2Index]/sum(matrix[word1Index])
  
def preent(str):
      sys.stdout.write(str)
      sys.stdout.flush()

def generateSentence(matrix, key, currentWord):
    sentence = currentWord
    while currentWord[-1] != '.':
      currentWordIndex = key.index(currentWord)
      wordChoices = matrix[currentWordIndex]
      wordWeights = list(map(lambda x: x/sum(wordChoices), wordChoices))
      choice = random.choices(key, wordWeights, k=1)[0]
      sentence = sentence + ' '  + choice
      currentWord = choice
    return sentence
    
if __name__ == "__main__":
  text = getScript()
  #text = "hello world my name is boxxy and my world is big hello to everyone to me everyone is nice is boxxy"
  key = getKey(text)
  matrix = occurrenceMatrix(key, text)
  #preent("Got occurrenceMatrix\n")
  #pmatrix = probabilityMatrix(matrix)
  print(generateSentence(matrix, key, "A"))
  #print(pmatrix[key.index("I")][key.index("don't")])