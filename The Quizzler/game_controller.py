import requests as req
from random import randint
from json import *
import html

# Trivia API: 10 at a time, only booleans
TRIVIA_API_URL = "https://opentdb.com/api.php?amount=10&type=boolean"

# GameController controls all game logic and keeps score + question data
class GameController():
    def __init__(self) -> None:
        self.question = None
        self.correct_answer = None
        self.incorrect_answer = None
        self.score = 0

    # Pulls question data to the bank so the player can answer questions, 10 at a time
    def pull_question_data(self) -> dict:
        question_data = req.get(url=TRIVIA_API_URL)
        question_data.raise_for_status()
        question_data = question_data.json()

        # Formats data so it doesn't have the HTML shtuff
        for key in question_data["results"]:
            key["question"] = html.unescape(key["question"])
            key["category"] = html.unescape(key["category"])

        return question_data["results"]
    
    # Gets a question's data from the bank and deletes the key after so it isn't pulled again
    def get_question_from_bank(self) -> None:
        try:
            n = randint(0, len(self.question_bank)-1)
            self.question = self.question_bank[n]["question"]
            self.correct_answer = self.question_bank[n]["correct_answer"]
            self.incorrect_answer = self.question_bank[n]["incorrect_answers"]
            self.remove_question_from_bank(n)
        
        # If the bank is missing, or has ran dry, it'll re-pull automatically
        except (AttributeError, ValueError):
            self.question_bank = self.pull_question_data()
            self.get_question_from_bank()
    
    # Removes the question key from the bank so it isn't pulled again
    def remove_question_from_bank(self, key: int) -> None:
        del self.question_bank[key]

    # Accepts answers from the player via the UI and returns the value to the UI
    def accept_answer(self, answer: str) -> bool:
        is_correct = answer == self.correct_answer
        if is_correct:
            self.score += 1
        return is_correct