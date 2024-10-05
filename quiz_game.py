import csv
import json
import random
from termcolor import cprint


def quiz_game():

    with open('quiz.json', 'r') as f:
        questions = json.load(f)

    random.shuffle(questions)
    sum = 0
    user_choice = input("choose category: (h/s/m): ")
    if user_choice == 'h':
        questions = [
            question for question in questions if question['category'] == 'history']

    for index, item in enumerate(questions, start=1):

        print(f"Question {index}: {item['question']}")
        answer = input("Answer: ")
        if answer == item['answer']:
            sum += 1
            cprint("Correct...!!", 'green')
        else:
            cprint(f"Sorry..wrong answer, the correct one is {
                   item['answer']}", 'red')

    print(f"Your final score: {sum}/{len(questions)}")


def convert_json_to_csv():
    questions = []
    # how to convert a json file to csv format
    with open('questions.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            row['options'] = row['options'].split(', ')
            questions.append(row)


quiz_game()
