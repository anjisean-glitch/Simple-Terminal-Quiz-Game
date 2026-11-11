import requests
import random


print("Hello there!!")
print("=" * 20)

name = input("What is your name: ")
print("=" * 20)

print(f"Its nice to meet you, {name}")
print("=" * 20)



## retrieving type from user
question_type = input(f"What type of question would you like {name}?\n1. Multiple\n2. True/False\nPlease Select 1 or 2: ")
print("=" * 20)

while not question_type.isdigit():
  print(f"Enter Only Numerical Values, '{name}'!!")
  print("=" * 20)
  question_type = input(f"What type of question would you like '{name}'?\n1. Multiple\n2. True/False\nPlease Select 1 or 2: ")
  print("=" * 20)

while question_type not in ["1", "2"]:
  print(f"Enter Either 1 or 2 {name}!!")
  print("=" * 20)
  question_type = input(f"What type of question would you like {name}?\n1. Multiple\n2. True/False\nPlease Select 1 or 2: ")
  print("=" * 20)

if question_type == "1":
  question_type = "multiple"
  

elif question_type == "2":
  question_type = "boolean"
  

## retrieving difficulty from user
difficulty = input(f"What level or difficulty would you like, '{name}'?\n1. Easy\n2. Medium\n3. Hard\nPlease Select Either 1, 2 or 3: ")
print("=" * 20)

while not difficulty.isdigit():
  print(f"Enter Only Numerical Values, '{name}'!!")
  print("=" * 20)
  difficulty = input(f"What level or difficulty would you like, '{name}'?\n1. Easy\n2. Medium\n3. Hard\nPlease Select Either 1, 2 or 3: ")
  print("=" * 20)

while difficulty not in ["1", "2", "3"]:
  print(f"Enter Either 1, 2 or 3, '{name}'!!")
  print("=" * 20)
  difficulty = input(f"What level or difficulty would you like, '{name}'?\n1. Easy\n2. Medium\n3. Hard\nPlease Select Either 1, 2 or 3: ")
  print("=" * 20)

if difficulty == "1":
  difficulty = "easy"

elif difficulty == "2":
  difficulty = "medium"

elif difficulty == "3":
  difficulty = "hard"


## retrieving number or questions from user

while True:
    try:
      print("=" * 20)
      amount = int(input("Enter the amount of questions: "))

      if 1 <= amount <= 50:
        break

      print("Enter a number between 1 and 50!")

    except ValueError:
      print("Enter numerical values only!")


## Retrieving categories from OpenTDB

category_url = "https://opentdb.com/api_category.php"

category_response = requests.get(category_url)
category_data = category_response.json()

categories = category_data["trivia_categories"]

print("\nAVAILABLE CATEGORIES")
print("=" * 30)

options = []
for index, category in enumerate(categories, start=1):
    print(f"{index}. {category['name']}")
    index = str(index)
    options.append(index)
    print(" -- ")


choice = input(f"Pick your choice, from 1 - {len(options)}: ")

while choice not in options:
  print("Enter a real choice")
  print("=" * 10)

  choice = input(f"Pick your choice, from 1 - {len(options)}: ")
  print("=" * 10)


final_choice = categories[int(choice) - 1]["id"]


# https://opentdb.com/api.php?amount=10&difficulty=hard&type=multiple


url = f"https://opentdb.com/api.php?amount={amount}&category={final_choice}&difficulty={difficulty}&type={question_type}"

response = requests.get(url)

print("=" * 20)
print(response.status_code)
print(f"Amount: {amount}\nDifficulty: {difficulty}\nType: {question_type}\nCategory: {final_choice}")
print("=" * 20)

data = response.json()

print(data)


results = data["results"]

score = 0

print(f"\nLETS START YOUR {amount} {difficulty} {question_type} choice type questions, {name}")
print("=" * 30)

for index, result in enumerate(results, start=1):
  question = result['question']

  correct_answer = result['correct_answer']


  wrong_answers = result['incorrect_answers']

  print(f"Question {index}")
  print(" = " * 10)
  print(question)
  # print("=" * 30)

  

  print("=" * 30)
  answers = wrong_answers + [correct_answer]
  random.shuffle(answers)

  if question_type == "multiple":
    letters = ["A", "B", "C", "D"]
  else:
    letters = ["1", "2"]

  for option, answer in zip(letters, answers):
    print(f"{option}. {answer}")

  print("=" * 30)

  if question_type == "multiple":
    letter_choice = input("Input your answer (A-D): ").upper()
    print("=" * 30)

    while letter_choice not in letters:
      print("Your answer should be A, B, C or D.")
      print("=" * 30)
      letter_choice = input("Input your answer (A-D): ").upper()
      print("=" * 30)

  else:
    letter_choice = input("Input your answer (1-2): ")
    print("=" * 30)

    while letter_choice not in letters:
      print("Your answer should be 1 or 2.")
      print("=" * 30)
      letter_choice = input("Input your answer (1-2): ")
      print("=" * 30)

  # Shared answer-checking and scoring logic
  selected_answer = answers[letters.index(letter_choice)]
  correct_index = answers.index(correct_answer)

  if selected_answer == correct_answer:
    print("You got it!!!")
    score += 1
  else:
    print("You failed it!!!")

  print(f"Correct Answer: {letters[correct_index]}\\n-- {correct_answer}")
  print("=" * 20)
  print(f"Total Score: {score}/{index}")


##### BY ANJI BOB-MANUEL #####################################

