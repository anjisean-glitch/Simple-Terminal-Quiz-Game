# Simple Terminal Quiz Game

A Python command-line quiz game that retrieves trivia questions from the [Open Trivia Database (OpenTDB)](https://opentdb.com/). Choose your question format, difficulty, category, and how many questions you want to answer.

## Features

- Choose between **Multiple Choice** and **True/False** questions.
- Select a difficulty: **Easy**, **Medium**, or **Hard**.
- Choose from the categories provided by the Open Trivia Database.
- Select between **1 and 50 questions** for a quiz.
- Answer options are shuffled before they are displayed.
- Receive feedback after submitting an answer.
- View your score as you progress through the quiz.

## Built With

- **Python**
- **Requests** – makes HTTP requests to the Open Trivia Database API.
- **Open Trivia Database API** – supplies the trivia categories and questions.

## Requirements

- Python 3.8 or later
- An internet connection
- The Python `requests` package

## Installation and Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/anjisean-glitch/Simple-Terminal-Quiz-Game.git
   ```

2. **Navigate into the project folder**

   ```bash
   cd Simple-Terminal-Quiz-Game
   ```

3. **Install the required package**

   ```bash
   python -m pip install requests
   ```

4. **Run the game**

   ```bash
   python quiz_game.py
   ```

## How to Play

1. Enter your name.
2. Choose Multiple Choice or True/False.
3. Select the difficulty level.
4. Enter the number of questions (between 1 and 50).
5. Choose a question category from the displayed list.
6. Read each question and enter the option that represents your answer.
7. Check the feedback and score displayed by the game.

## API

This project uses the [Open Trivia Database API](https://opentdb.com/api_config.php) to retrieve categories and questions.

- Categories endpoint: `https://opentdb.com/api_category.php`
- Questions endpoint: `https://opentdb.com/api.php`

The questions request is configured using the amount, category, difficulty, and question type selected by the player.

## Project Structure

```text
Simple-Terminal-Quiz-Game/
└── quiz_game.py
```

## Author

**Anji Bob-Manuel**

- GitHub: [@anjisean-glitch](https://github.com/anjisean-glitch)

---

This project was built as a practical exercise in Python, working with APIs, handling user input, and using data returned in JSON format.
