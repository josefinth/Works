from sys import displayhook
import math
import statistics

# Exercise 6: Test Average and Grade

score_list = []

def main():
    try:
        for i in range(5):
            test_score = float(input("Enter the testscore: "))
            score_list.append(test_score)

        determine_grade()
        print("The average score and grade equals: ", calc_average(score_list))

    except ValueError:
        print("The enterd value of the wrong type, enter flotat or int number")
        main()   

def calc_average(value_list:list):
    average = round(sum(value_list)/len(value_list),2)

    if 90 < average < 100:
        grade = 'A'
    elif 80 < average < 89:
        grade = 'B'
    elif 70 < average < 79:
        grade = 'C'
    elif 60 < average < 69:
        grade = 'D'
    elif average < 60:
        grade = 'E'
    else:
        print('Enter a test score in the range!')
    return average, grade


def determine_grade():
    for i in range(5):
        if score_list[i] > 90 and score_list[i] < 100:
            print('A')
        elif score_list[i] > 80 and score_list[i] < 89:
            print('B')
        elif score_list[i] > 70 and score_list[i] < 79:
            print('C')
        elif score_list[i] > 60 and score_list[i] < 69:
            print('D')
        elif score_list[i] < 60:
            print('F')
        else:
            print('Enter a test score in the range!')

main()
