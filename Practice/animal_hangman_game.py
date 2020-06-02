from random import randint
from termcolor import colored

def hangtheman(c):
    cman = {0:" +---+\n     |\n     |\n     |\n  ===",
            1:" +---+\n O   |\n     |\n     |\n  ===",
            2:" +---+\n O   |\n |   |\n     |\n  ===",
            3:" +---+\n O   |\n/|   |\n     |\n  ===",
            4:" +---+\n O   |\n/|\  |\n     |\n  ===",
            5:" +---+\n O   |\n/|\  |\n/    |\n  ===",
            6:" +---+\n O   |\n/|\  |\n/ \   |\n  ==="}
    return cman.get(c)

def pickaword():
    words = """ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra""".split(" ")
    word = words[randint(0,len(words))]
    return word

def validateletter(ch):
  while True:
    if ch.isalpha() == False:
      ch = input("\nThat's not a letter. Try again: ")
    elif len(ch) > 1:
      ch = input("\nThat's not a letter. Try again: ")
    elif ch in tried:
      ch = input("\nYou've already guessed this one! Pick another: ")
    else:
      return ch

print("Welcome to the animal themed HANGMAN game!")

word = pickaword()
missed = 0
tried = ""
guessed = ['_' for i in range(len(word))]

print("\nGuess this animal: \n\n" + " ".join(guessed) + "\n\n____________________________\n")

while True:
  ch = validateletter(input("\nPick a letter: ").lower())

  if ch.lower() in word:
    for i in [i for i, s in enumerate(word) if s == ch]:
      guessed[i] = ch    
    if "".join(guessed) == word:
      print(colored("\nYou did it! Good job!",'green'))
      print("\nThe word was " + word.upper())
      break
    else:
      print(colored("\nYou guessed a letter!\n", 'green'))

  else:
    print(colored("\nSorry, this letter isn't right!\n", 'magenta'))
    missed += 1        
    
  tried += ch

  print(hangtheman(missed))
  if "".join(guessed) != word and missed < 6:
    print("\n" + " ".join(guessed) + " : You have " + colored(str(6-missed),'yellow') + " tries left.")
    print("________________________________")
  elif missed >= 6: 
    print(colored("\nToo many tries, game over! The word was " + word.upper() , 'red'))
    break
  else:
    break
  
