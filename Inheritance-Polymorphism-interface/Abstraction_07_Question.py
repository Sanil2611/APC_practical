# Problem Statement:
# Create an abstract class Question with an abstract method evaluate_answer().
# Derive MCQQuestion, TrueFalseQuestion, and DescriptiveQuestion. Implement answer
# evaluation for each question type.

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def evaluate_answer(self, answer):
        return answer == "B"


class TrueFalseQuestion(Question):
    def evaluate_answer(self, answer):
        return answer.lower() == "true"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        return len(answer.strip()) > 20


questions = [MCQQuestion(), TrueFalseQuestion(), DescriptiveQuestion()]

answers = ["B", "true", "This is a descriptive answer with sufficient detail."]

for question, answer in zip(questions, answers):
    print("Correct:", question.evaluate_answer(answer))
