import random
from random import choice

def scrape():
    file = open('questions_list1.txt', 'r+')
    lines = [line for line in file.readlines()]
    file.close()

    q1 = choice(lines)
    return q1

def scrape2():
    file = open('questions_list2.txt', 'r+')
    lines = [line for line in file.readlines()]
    file.close()

    q2 = choice(lines)
    return q2    