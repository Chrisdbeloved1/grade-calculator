### GRADE CALCULATOR

## Usage
Have you ever wondered what your final grade will be? Do you want to make sure you're on track to getting the grade you want? Well, the Grade Calculator is here to help!

Let's say you have a math class and your final grade is based on three categories: assignments, quizzes, and exams. You received a score of 80% on your assignments, 90% on your quizzes, and 85% on your exams. But wait, your assignments were worth 40% of your grade, your quizzes were worth 30%, and your exams were worth 30%. How do you calculate your final grade?

That's where the Grade Calculator comes in handy! By inputting your scores and weights for each category, you can see what your final grade will be. The Grade Calculator will calculate your final grade and display it in the grade table below the input fields.

## Task and Hints

# Task
The calculate_grade() function is currently empty and needs to be filled out in order for the grade calculator to work properly. If you run the code now, you you ll see a python GUI screen pop up on your screen, you should be able to input your grades score and weight. But when you click on calculate, you wont get any output becasue your calculate_grade() function is still empty. 
Your task is to complete this function as part of your project. The function should calculate the final grade based on the scores and weights entered by the user.

# Hints
In order to calculate your final grade, you need to take the score for each category, multiply it by its weight, and add them all together then divide everything by the sum of the weights. To do this, you need to create variables to retrieve all the scores and weight from the GUI. Here is an example code snippet to guide you:

final_grade = (assignments_score * assignments_weight + quizzes_score * quizzes_weight + exams_score * exams_weight) / (assignments_weight + quizzes_weight + exams_weight)

This code snippet takes the score for each category (assignments_score, quizzes_score, exams_score), multiplies it by its weight (assignments_weight, quizzes_weight, exams_weight), and adds them all together. Then, it divides everything by the sum of the weights to obtain the final grade.

Don't worry if this seems a bit tricky at first! Working on this project will help you learn more about Python GUI programming, using tkinter and ttk modules. You'll gain knowledge on creating GUI windows, input fields, buttons, and tables. This knowledge will help you create more complex and useful applications in the future.
