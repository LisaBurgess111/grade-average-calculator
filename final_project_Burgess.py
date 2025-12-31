#Lisa Burgess


#Calculates the average of the grades input by the user
def calc_average_grade():
    grades_sum = 0
    num_grades = 0
    for grade in grades_list:
        grades_sum += grade
        num_grades += 1
    average_grade = grades_sum / num_grades
    return average_grade


#Prints a statement judging the average of the grades input by the user
def judge_average():
    if calc_average_grade() >= 95:
        print("Doing wonderfully!")
    elif calc_average_grade() >= 85:
        print("Doing good!")
    elif calc_average_grade() >= 75:
        print("Could use improvement")
    elif calc_average_grade() >= 65:
        print("Barely passing")
    else:
        print("Failing")


#Main part of program
if __name__ == "__main__":

    #Creates a list of grades input by the user and defines input_grade
    grades_list = []
    input_grade = input("Input grades. Type 'done' to calculate the average of the grades.")


    #Runs code inside loop while input grade
    #is not equal to "done"
    while input_grade != "done":

        #Converts user input to float, updates
        #grades_list, and clears input field
        try:
            input_grade = float(input_grade)
            grades_list.append(input_grade)
            input_grade = input()


        #Handles ValueError and clears input field
        except ValueError:
            print("Input must be a number or 'done'.")
            input_grade = input()

    #prints output of the program
    print(f"Average grade is {calc_average_grade():.1f}")
    judge_average()
