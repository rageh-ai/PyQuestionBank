from excelProcessing import *

while True:
    user_name = input("Please Enter Your Username (enter q to quit): ")
    user_password = input("Please Enter Your Password (enter q to quit): ")
    view_results = "n"

    if user_name == "q" or user_password == "q":
        exit()

    valid_user = username_validation(user_name)
    valid_password = password_validation(user_password)

    if valid_password and valid_user:
        print_user_data(user_name)
        while view_results == "n":

            chosen_quiz = validate_available_quizzes()
            results_data = start_quiz(chosen_quiz, user_name)
            add_quiz_results(results_data)
            quiz_score = get_quiz_score()
            add_taken_quiz_user_profile(user_name, chosen_quiz, quiz_score)
            print(f"You scored {quiz_score}% in the {chosen_quiz} quiz")
            view_results = input("Would you like to view the quiz answers (y/n): ")
            if view_results == "y":
                print_results(user_name, chosen_quiz)
                clear_results()
                exit()
            elif view_results == "q":
                clear_results()
                exit()
            clear_results()
    elif not(valid_password and valid_user):
        print ("There does not appear to be a user who matches these credentials")
        store_user_info()
























