import random
from random import choice
import time

interview_questions = [
    'A', 'B', 'C', 'D'
]

def find_questions(arr):
    question1 = choice(arr)
    question2 = choice(arr)
    return question1, question2

questions = find_questions(interview_questions)
first_q = questions[0]
second_q = questions[1]

def print_questions(str1, str2):
    print(f"Vallie, {str1}?")
    time.sleep(2)
    print(f"Vallie, {str2}?")

print_questions(first_q, second_q)

practice_dict = {'Question One': first_q,
                 'Question Two': second_q
                 }
