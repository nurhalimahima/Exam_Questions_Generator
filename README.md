## README for Github - Questions and Answers Quiz
This Python code is a simple quiz game that asks the user a set of randomized questions and scores their answers. The questions and answers are read from an Excel file and shuffled to ensure that the user receives a different set of questions each time they play. The code uses the Levenshtein distance algorithm to score the user's answers based on how similar they are to the correct answer.

## Getting Started
To run this code, you will need Python 3.x installed on your machine and an Excel file with a list of questions and answers.

1. Clone the repository to your local machine using git clone https://github.com/<username>/<repository_name>.git
2. Install the required libraries using pip install -r requirements.txt
3. Replace questions_answers.xlsx with your own Excel file containing questions and answers.
4. Run the code using python quiz.py.

## How to Play
1. Run the code using python quiz.py.
2. Answer the questions that are presented to you one at a time.
3. Your score will be presented to you at the end of the quiz.

## How it Works
1. The code reads the questions and answers from an Excel file using the pandas library.
2. The questions and answers are shuffled using the sample method.
3. The code presents each question to the user and prompts them for an answer using the input function.
4. The user's answer is compared to the correct answer using the Levenshtein distance algorithm.
5. If the user's answer is an exact match, they receive 2 points. If the answer is similar but not exact, they receive 1 point. If the answer is incorrect, they receive 0 points.
6. The user's score is presented at the end of the quiz.

## Dependencies
* Python 3.x
* pandas
* Levenshtein

## License
Nothing special.
