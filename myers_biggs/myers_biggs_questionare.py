extroversion_introversion_test = ["A. expend energy, enjoy groups. B. conserve energy, enjoy one-on-one: ",
                                  "A. more outgoing, think out loud. B. more reserved, think to yourself:",
                                  "A. seek many tasks, public activities, interaction with others. " +
                                  "B. seek private, solitary activities with quiet to concentrate,: ",
                                  "A.external, communicative, express yourself. B. internal, reticent, keep to "
                                  "yourself: ",
                                  "A. active, initiate. B. reflective, deliberate: "]

sensing_intuition_test = ["A. interpret literally. B. look for meaning and possibilities",
                          "A. practical, realistic, experiential. B. imaginative, innovative, theoretical",
                          "A. standard, usual, conventional. B. different, novel, unique",
                          "A. focus on here-and-now\" .B.look to the future, global perspective, \"big picture\"",
                          "A. facts, things, \"what is\". B. ideas, dreams, \"what could be,\" philosophical"]

thinking_feeling_test = ["A. logical, thinking, questioning. B. empathetic, feeling, accommodating",
                         "A. candid, straight forward, frank. B.tactful, kind, encouraging",
                         "A. firm, tend to criticize, hold the line. B. gentle, tend to appreciate, conciliate",
                         "A. tough-minded, just B.tender-hearted, merciful",
                         "A. matter of fact, issue-oriented B. sensitive, people-oriented, compassionate"]

judging_perceiving_test = ["A. organized, orderly. B. flexible, adaptable",
                           "A. plan, schedule B. unplanned, spontaneous",
                           "A. regulated, structured B. easygoing, \"live\" and \"let live\"",
                           "A. preparation, plan ahead. B. go with the flow, adapt as you go",
                           "A. control, govern B. latitude, freedom"]
test_result = []
counter_1 = 0
extroversion_introversion_list = []
valid_input = ["a", "b"]
while counter_1 < 5:
    user_input = input(extroversion_introversion_test[counter_1])
    if user_input not in valid_input:
        print("Invalid input")
    else:
        extroversion_introversion_list.append(user_input)
        counter_1 += 1

if "a" > "b" in counter_1:
    answer = "E"
else:
    answer = "I"
test_result.append(answer)

counter_2 = 0
sensing_intuition_list = []
while counter_2 < 5:
    user_input = input(sensing_intuition_test[counter_2])
    if user_input not in valid_input:
        print("Invalid input")
    else:
        sensing_intuition_list.append(user_input)
        counter_2 += 1
if "a" > "b" in counter_2:
    answer = "S"
else:
    answer = "N"
test_result.append(answer)

counter_3 = 0
thinking_feeling_list = []
while counter_3 < 5:
    user_input = input(thinking_feeling_test[counter_3])
    if user_input not in valid_input:
        print("Invalid input")
    else:
        thinking_feeling_list.append(user_input)
        counter_3 += 1
if "a" > "b" in counter_3:
    answer = "T"
else:
    answer = "F"
test_result.append(answer)

counter_4 = 0
judging_perceiving_list = []
while counter_4 < 5:
    user_input = input(judging_perceiving_test[counter_4])
    if user_input not in valid_input:
        print("Invalid input")
    else:
        judging_perceiving_list.append(user_input)
        counter_4 += 1
if "a" > "b" in counter_1:
    answer = ""
else:
    answer = "P"
test_result.append(answer)

print(test_result)
                                                                                         