headings = ["STUDENT", 'SUB1', "SUB2", 'SUB3', "TOT", "AVE", "POS"]
student = int(input("Enter score for subject: "))
subject = int(input("Enter score for second subject: "))
# sub_3 = int(input("Enter score for third subject: "))
total_1 = (sub_1 + sub_2)
student_1_pos = 0
AAaverage_1 = total_1 / 3.0


student_2 = input("Second student name: ")
sub_i = int(input("Enter score for subject: "))
sub_ii = int(input("Enter score for second subject: "))
sub_iii = int(input("Enter score for third subject: "))
total_i = (sub_i + sub_ii + sub_iii)
average_i = (total_i / 3)
student_2_pos = 0
studentii = [student_2, sub_i, sub_ii, sub_ii, total_i, average_i]
import math

student_3 = input("Third student name: ")
subj_1 = int(input("Enter score for subject: "))
subj_2 = int(input("Enter score for second subject: "))
subj_3 = int(input("Enter score for third subject: "))
total_i1 = (subj_1 + subj_2 + subj_3)
average_i1 = (total_i1 / 3)
student_3_pos = 0
subjectiii = [student_3, subj_1, subj_2, subj_3, total_i1, average_i1]
now = 'yrtttettey'
print(f'okay {now:>60}')

print(headings[0],"\t", headings[1],"\t", headings[2],"\t", headings[3],"\t", headings[4],"\t", headings[5],"\t", headings[6])
print(student_1,"\t", sub_1,"\t", sub_2,"\t", total_1,"\t", round(average_1),"\t", student_1_pos)
print(student_2,"\t", sub_i,"\t", sub_ii,"\t",  sub_iii,"\t", total_i,"\t", round(average_i),"\t", student_2_pos)
print(student_3,"\t", subj_1,"\t", subj_2,"\t", subj_3,"\t", total_i1,"\t", round(average_i1),"\t", student_3_pos)
#for heading in headings:
#      print(heading, end='\t \t \t')
# print(" ")
# for student in studenti:
#      print(student, end='\t \t \t')

# marks = [1, 23, 45, 56, 44, 48]
# current_rank = 0
# global_rank = 0
# current_mark = 0

# for mark in marks:
#     global_rank += 1
#     if mark != current_mark:
#         current_mark = mark
#         current_rank = global_rank
#     print(current_mark, current_rank)