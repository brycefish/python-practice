#!/usr/bin/env python3
# Bryce Fish
# Lab 6-1 
# Sep 6th


def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    score_total = 0
    
    for score in scores:
        score_total += score

    average = round(score_total / len(scores))
    
    # calculate high and low
    low_score = min(scores)
    high_score = max(scores)

    #get median for both odd/even 
    median_index = len(scores) // 2
    if len(scores) % 2 == 1:
        median = scores[median_index]
    else:
        even1 = scores[median_index]
        even2 = scores[median_index - 1]
        median = (even1 + even2) / 2

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye Bye Now!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


