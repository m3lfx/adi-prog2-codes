def main():
    score1 = int(input("enter score 1: "))
    score2 = int(input("enter score 2: "))
    score3 = int(input("enter score 3: "))
    score4 = int(input("enter score 4: "))
    score5 = int(input("enter score 5: "))

    average_score = calc_average(score1, score2, score3, score4, score5)

    letter_grade = determine_grade(average_score)
    print(f"your final grade of {average_score} in letter equivalent is {letter_grade}")

        

def calc_average(sc1, sc2, sc3, sc4,sc5):
   
    average = (sc1 + sc2 + sc3 + sc4 +sc5) / 5.0
    return average

def determine_grade(score):
    letter = ""
    if score >= 90 and score <= 100:
        letter = 'A'
        
       
    elif score >= 80 and score <= 89:
        letter = 'B'
        
    elif score >= 70 and score <= 79:
        letter = 'C'
        
    elif score >= 60 and score <= 69:
        letter = 'D'
    
    elif score >= 0 and score <= 59:
        letter = 'F'
        
    else:
        letter = "invalid input"
    
    return letter
    

main()