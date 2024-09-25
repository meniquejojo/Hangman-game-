import random

hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ___|___
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ___|___
    """
]

words = ('testing', 'javascript', 'simple')
word = random.choice(words)

def hangman(word, hangman_stages):
    wrong = 0
    guesses = 0
    guessed_word = []
    print('This is a hangman game')

    while wrong < len(hangman_stages) - 1:
        guesses += 1
        # Display the current state of the guessed word
        display = ''.join(letter if letter in guessed_word else '_ ' for letter in word)
        print('Word:', display)
        
        ans = input('Please enter one letter: ')
        while len(ans) != 1:
            print('ONE LETTER!!')
            ans = input('Please enter one letter: ')

        if ans in word:
            if ans not in guessed_word:  # Only append if the letter hasn't been guessed yet
                guessed_word.append(ans)
                print('You got the answer correct!')
                
            else:
                print('You already guessed that letter')
        else:
            wrong += 1
            print('You guessed the wrong word')
            print(hangman_stages[wrong])
            

        if len(display)-1 == len(word):
            print(f'Congratulations, you guessed the word "{word}" in {guesses} guesses!')
            break

    if wrong == len(hangman_stages) - 1:
        print('Your hangman has died !!!')
        print('You failed this round')
        print(f'The correct word is: "{word}"')


hangman(word, hangman_stages)