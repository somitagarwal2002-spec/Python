# Dictionary Comprehension

# new_dict = {new_key:new_value for item in list}  Syntax for list
# new_dict = {new_key:new_value for (key,value) in dict.items()}  Syntax for existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}  With Condition

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_student = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_student)
