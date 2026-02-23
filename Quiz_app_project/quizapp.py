import random
import time
def run_quiz():
    questions = [
        {
            "prompt": "What is the capital city of Nepal?",
            "options": ["A) New Delhi", "B) Beijing", "C) Pokhara", "D) Kathmandu"],
            "answer": "D"
        },
        {
            "prompt": "Which programming language is known as the snake langauge?",
            "options": ["A) Java", "B) C++" "C) Python", "D) Ruby"],
            "answer": "C)"
        },
        {
            "prompt": "Which planet in the solar system is known as the 'Red Planet'?",
            "options": ["A) Mars", "B) Venus", "C) Jupiter", "D) Pluto"],
            "answer": "A)"
        },
        {
            "prompt": "Which country's flag is the only non-rectangular flag in the world?",
            "options": ["A) USA", "B) Switzerland" "C) Nepal" "D) Vatican City"],
            "answer": "C)"
        },
        {
            "prompt": "Who created the python programming language?",
            "options": ["A) Guido Van Rossum", "B) Dennis Ritchie", "C) Tim Berners-Lee", "D) Linus Torvalds"],
            "answer": "A)"
        },
        {
            "prompt": "The 2026 FIFA world cup will be the first to be hosted by three different countrires. Which ones are they?",
            "options": ["A) Brazil, Argentina, Uruguay", "B) Spain, Portugal and Morocco", "C) China, Japan and South Korea", "D) USA, Canada and Mexico"],
            "answer": "D)"
        }
]
    random.shuffle(questions)

    score = 0
    total_questions = len(questions)