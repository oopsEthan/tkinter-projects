import requests as req
from random import randint
from json import *

TRIVIA_API_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

class Question_Generator():
    def __init__(self) -> None:
        self.correct_answer = None
        self.incorrect_answer = None
        self.question = None
        self.question_bank = self.generate_question_data()
        self.format_question_data()
        self.generate_new_question()

    def generate_question_data(self) -> dict:
        question_data = req.get(url=TRIVIA_API_URL)
        print("Question data pulled.")
        question_data.raise_for_status()
        return question_data.json()["results"]

    def format_question_data(self) -> None:
        for key in self.question_bank:
            key["category"] = key["category"].replace("&amp;", "&")
            key["question"] = key["question"].replace("&quot;", "'")
            key["question"] = key["question"].replace("&#039;", "'")
            self.dump_data_to_file()

    def dump_data_to_file(self) -> None:
        with open("question_data.json", "w") as data:
            dump(self.question_bank, data, indent=4)

    def generate_new_question(self) -> None:
        n = randint(0, len(self.question_bank)-1)
        print(f"{n}/{len(self.question_bank)}")
        self.question = self.question_bank[n]["question"]
        self.correct_answer = self.question_bank[n]["correct_answer"]
        self.incorrect_answer = self.question_bank[n]["incorrect_answers"]
    
    def submit_answer(self, answer) -> bool:
        if answer == self.correct_answer:
            return True
        return False