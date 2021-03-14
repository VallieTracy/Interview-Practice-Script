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
    
    q1 = choice(my_list)
    return q1
    

def scrape2():
    # interview_questions = ['A', 'B', 'C', 'D']
    
    # q1 = choice(interview_questions)
    # return f"Q1 = {q1}"
    my_list = []

    file = 'questions2.py'
    with open(file, 'r') as text:
        lines = text.read().replace('\n', '')
        for line in lines:
            my_list.append(line)
    
    q2 = choice(my_list)
    return q2

def scrape3():
    for i in range(0, 3):
        print(i)


    
    

    





# my_list = []

# file = 'questions.py'
# with open(file, 'r') as text:
#     lines = text.read().replace('\n', '')
#     for line in lines:
#         my_list.append(line)
# print(my_list)





