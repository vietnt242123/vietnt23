"""
Program: page_151_casestydy_01.py
Author: NGUYEN TAN VIET
Date: 09/10/2021

Problen:
    Generates and displays sentences using simple grammar
    and vocabulary. Words are chosen at random.
Solution:

Enter the number of sentences: 3
THE BOY HIT THE BOY BY A BALL
A BOY HIT THE GIRL WITH THE BALL
A BALL LIKED A GIRL WITH THE BOY

"""
import random

# Từ vựng: các từ trong 4 phần khác nhau của bài phát biểu

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()


def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number)
        print(sentence())

if __name__== '__main__':
    main()

