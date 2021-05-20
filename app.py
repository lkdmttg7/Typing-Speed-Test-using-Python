import sys
import time
import random

def get_sentence(self):
    f = open('sentences.txt').read()
    sentences = f.split('\n')
    sentence = random.choice(sentences)
    return sentence
def draw_text(self, screen, msg, y ,fsize, color):
    font = pygame.font.Font(None, fsize)
    text = font.render(msg, 1,color)
    text_rect = text.get_rect(center=(self.w/2, y))
    screen.blit(text, text_rect)
    pygame.display.update()
