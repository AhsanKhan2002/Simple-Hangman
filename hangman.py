import random
from words import word_list


def get_word():
  word = random.choice(word_list)
  return word.upper()


def play(word):
  wordlength = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Welcome to Hangman")
  print(display_hangman(tries))
  print(wordlength)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Please input a letter or word as your guess ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You already guessed", guess)
      elif guess not in word:
        print(guess, "is not in the word")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Spectacular! ", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(wordlength)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        wordlength = "".join(word_as_list)
        if "_" not in wordlength:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed the word", guess)
      elif guess != word:
        print(guess, "is not the word")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        wordlength = word
    elif len(guess) == len(word) and guess.isalpha():
      x = 0
    else:
      print("Invalid Guess! You guess is either too long or not an alphabet. Please Try Again!")
    print(display_hangman(tries))
    print(wordlength)
    print("\n")
  if guessed:
    ("CONGRATULATIONS! You have guessed the word correctly! You win!")
  else:
    print("Awee Sorry! You ran out of tries. The word was " + word +
          ". Better luck next time!")


def display_hangman(tries):
  stages = [  # final state: head, torso, both arms, and both legs
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    # head, torso, both arms, and one leg
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
    # head, torso, and both arms
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
    # head, torso, and one arm
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
    # head and torso
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
    # head
    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
    # initial empty state
    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
  ]
  return stages[tries]


def main():
  word = get_word()
  play(word)
  while input("Play Again ? (Y/N) ").upper() == "Y":
    word = get_word
    play(word)


if __name__ == "__main__":
  main()
