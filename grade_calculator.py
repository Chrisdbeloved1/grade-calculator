import tkinter as tk
from tkinter import ttk

# Function to calculate final grade
def calculate_grade():
    pass
    # Write your code here.

# Create GUI window
root = tk.Tk()
root.title("Grade Calculator")

# Create input fields
assignments_label = ttk.Label(root, text="Assignments Score:")
assignments_label.grid(row=0, column=0)
assignments_entry = ttk.Entry(root)
assignments_entry.grid(row=0, column=1)

quizzes_label = ttk.Label(root, text="Quizzes Score:")
quizzes_label.grid(row=1, column=0)
quizzes_entry = ttk.Entry(root)
quizzes_entry.grid(row=1, column=1)

exams_label = ttk.Label(root, text="Exams Score:")
exams_label.grid(row=2, column=0)
exams_entry = ttk.Entry(root)
exams_entry.grid(row=2, column=1)

assignments_weight_label = ttk.Label(root, text="Assignments Weight:")
assignments_weight_label.grid(row=3, column=0)
assignments_weight_entry = ttk.Entry(root)
assignments_weight_entry.grid(row=3, column=1)

quizzes_weight_label = ttk.Label(root, text="Quizzes Weight:")
quizzes_weight_label.grid(row=4, column=0)
quizzes_weight_entry = ttk.Entry(root)
quizzes_weight_entry.grid(row=4, column=1)

exams_weight_label = ttk.Label(root, text="Exams Weight:")
exams_weight_label.grid(row=5, column=0)
exams_weight_entry = ttk.Entry(root)
exams_weight_entry.grid(row=5, column=1)

# Create calculate button
calculate_button = ttk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=6, column=1)

# Create grade table
grade_table = ttk.Treeview(root, columns=("Assignments Score", "Quizzes Score", "Exams Score", "Final Grade"))
grade_table.heading("Assignments Score", text="Assignments Score")
grade_table.heading("Quizzes Score", text="Quizzes Score")
grade_table.heading("Exams Score", text="Exams Score")
grade_table.heading("Final Grade", text="Final Grade")
grade_table.grid(row=7, column=0, columnspan=2)

# Run GUI window
root.mainloop()
