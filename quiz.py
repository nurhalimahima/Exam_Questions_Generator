import random
import pandas as pd
import Levenshtein

# Load the questions and answers from an Excel file
q_a_df = pd.read_excel("questions_answers.xlsx")

# Shuffle the questions and answers
q_a_df = q_a_df.sample(n=5).reset_index(drop=True)

# Score the user's answers
score = 0
for _, row in q_a_df.iterrows():
    print("================================================================================================")
    question = row["question"]
    answer = row["answer"]
    user_answer = input(question + "\n")
    print("================================================================================================")
    # Calculate the Levenshtein distance between the user's answer and the correct answer
    lev_distance = Levenshtein.distance(user_answer.lower(), answer.lower())
    # If the Levenshtein distance is less than or equal to 3 (i.e. the answers are similar but not exact),
    # count the answer as partially correct and give half the points
    if lev_distance <= 3:
        print(f"Partially correct! The correct answer is: {answer}")
        score += 1
    # If the Levenshtein distance is 0 (i.e. the answers are exactly the same),
    # count the answer as fully correct and give full points
    elif lev_distance == 0:
        print("Correct!")
        score += 2
    # Otherwise, count the answer as incorrect and give no points
    else:
        print(f"Incorrect. The correct answer is: {answer}")

# Print the user's score
print("================================================================================================")
print(f"Your score is {score}/{len(q_a_df)*2}")
