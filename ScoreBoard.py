import pandas
student_dict = {"student" : ["angela", "james", "lily"], "score" : [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "lily":
        print(row.score)