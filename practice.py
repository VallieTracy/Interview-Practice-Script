import random
from random import choice
import time

def scrape():
    # interview_questions = ['A', 'B', 'C', 'D']
    
    # q1 = choice(interview_questions)
    # return f"Q1 = {q1}"
    my_list = []

    file = 'questions.py'
    with open(file, 'r') as text:
        lines = text.read().replace('\n', '')
        for line in lines:
            my_list.append(line)
    return f"{my_list}"





# my_list = []

# file = 'questions.py'
# with open(file, 'r') as text:
#     lines = text.read().replace('\n', '')
#     for line in lines:
#         my_list.append(line)
# print(my_list)





