import sys
import time
import random

def get_sentence(self):
    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    return sentence
