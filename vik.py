task1 = ' school work'
task2 = ' home work '
task3 = ' leisure '
task4 = ' sleep '
TIME = {1:'X', 2:'X', 3:'X', 4:'X', 5:'X', 6:'X', 7:'X', 8:'X', 9:'X', 10:'X',
        11:'X', 12:'X', 13:'X', 14:'X', 15:'X', 10:'X', 17:'X', 18:'X', 19:'X', 20:'X',
        21:'X', 22:'X', 23:'X', 24:'X'}
NAME=input("Enter your name:-")
READY_YES_NO = input("Do you want to make a schedule? Type 'yes' or 'no': ").lower()

if READY_YES_NO == 'yes':
    USER_TASK1=input(task1,task2,task3)
    INPUT_TIME_FIRST = input("(1)  Enter the time from "
                                     " where you want to start,\n"
                                     "your first task (ex:1,2....24)\n"
                                     "(in numbers):\n")
    if INPUT_TIME_FIRST.isdigit():
       INPUT_TIME_second=input("(2)  Enter the time when "
                                     " you want to end,\n"
                                     "your paticular task (ex:1,2....24)\n"
                                     "(in numbers):\n")
       print(INPUT_TIME_FIRST,' TILL ',INPUT_TIME_second)
    else:
                print('only positive integers')

else:
    print("You chose not to make a schedule.")
