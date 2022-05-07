# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5, 3, 2, 7, 5]


survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]


result = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

# 문제수만큼 반복한다
for i in range(len(survey)):
    # i번째 문제는
    if survey[i] == "AN":
        if choices[i] == 1:
            result["A"] += 3
        elif choices[i] == 2:
            result["A"] += 2
        elif choices[i] == 3:
            result["A"] += 1
        elif choices[i] == 4:
            result["A"] += 0
            result["N"] += 0
        elif choices[i] == 5:
            result["N"] += 1
        elif choices[i] == 6:
            result["N"] += 2
        else: # choices[i] == 7
            result["N"] += 3

    elif survey[i] == "NA":
        if choices[i] == 1:
            result["N"] += 3
        elif choices[i] == 2:
            result["N"] += 2
        elif choices[i] == 3:
            result["N"] += 1
        elif choices[i] == 4:
            result["N"] += 0
            result["A"] += 0
        elif choices[i] == 5:
            result["A"] += 1
        elif choices[i] == 6:
            result["A"] += 2
        else: # choices[i] == 7
            result["A"] += 3

    elif survey[i] == "CF":
        if choices[i] == 1:
            result["C"] += 3
        elif choices[i] == 2:
            result["C"] += 2
        elif choices[i] == 3:
            result["C"] += 1
        elif choices[i] == 4:
            result["C"] += 0
            result["F"] += 0
        elif choices[i] == 5:
            result["F"] += 1
        elif choices[i] == 6:
            result["F"] += 2
        else: # choice[i] == 7
            result["F"] += 3

    elif survey[i] == "FC":
        if choices[i] == 1:
            result["F"] += 3
        elif choices[i] == 2:
            result["F"] += 2
        elif choices[i] == 3:
            result["F"] += 1
        elif choices[i] == 4:
            result["F"] += 0
            result["C"] += 0
        elif choices[i] == 5:
            result["C"] += 1
        elif choices[i] == 6:
            result["C"] += 2
        else: # choices[i] == 7
            result["C"] += 3

    elif survey[i] == "MJ":
        if choices[i] == 1:
            result["M"] += 3
        elif choices[i] == 2:
            result["M"] += 2
        elif choices[i] == 3:
            result["M"] += 1
        elif choices[i] == 4:
            result["M"] += 0
            result["J"] += 0
        elif choices[i] == 5:
            result["J"] += 1
        elif choices[i] == 6:
            result["J"] += 2
        else: # choices[i] == 7
            result["J"] += 3

    elif survey[i] == "JM":
        if choices[i] == 1:
            result["J"] += 3
        elif choices[i] == 2:
            result["J"] += 2
        elif choices[i] == 3:
            result["J"] += 1
        elif choices[i] == 4:
            result["J"] += 0
            result["M"] += 0
        elif choices[i] == 5:
            result["M"] += 1
        elif choices[i] == 6:
            result["M"] += 2
        else: # choices[i] == 7
            result["M"] += 3

    elif survey[i] == "TR":
        if choices[i] == 1:
            result["T"] += 3
        elif choices[i] == 2:
            result["T"] += 2
        elif choices[i] == 3:
            result["T"] += 1
        elif choices[i] == 4:
            result["T"] += 0
            result["R"] += 0
        elif choices[i] == 5:
            result["R"] += 1
        elif choices[i] == 6:
            result["R"] += 2
        else: # choices[i] == 7
            result["R"] += 3
    else: # survey[i] == "RT"
        if choices[i] == 1:
            result["R"] += 3
        elif choices[i] == 2:
            result["R"] += 2
        elif choices[i] == 3:
            result["R"] += 1
        elif choices[i] == 4:
            result["R"] += 0
            result["T"] += 0
        elif choices[i] == 5:
            result["T"] += 1
        elif choices[i] == 6:
            result["T"] += 2
        else: # choices[i] == 7
            result["T"] += 3

RT_type = dict()
CF_type = dict()
JM_type = dict()
AN_type = dict()

RT_type["R"] = result["R"]
RT_type["T"] = result["T"]
CF_type["C"] = result["C"]
CF_type["F"] = result["F"]
JM_type["J"] = result["J"]
JM_type["M"] = result["M"]
AN_type["A"] = result["A"]
AN_type["N"] = result["N"]

# print(RT_type)
# print(CF_type)
# print(JM_type)
# print(AN_type)

answer = ''
a = ''
b = ''
c = ''
d = ''

for type_survey, score_choices in RT_type.items():
    if RT_type["R"] == RT_type["T"]:
        a = "R"
    elif max(RT_type.values()) == score_choices:
        a = type_survey

for type_survey, score_choices in CF_type.items():
    if CF_type["C"] == CF_type["F"]:
        b = "C"
    elif max(CF_type.values()) == score_choices:
        b = type_survey

for type_survey, score_choices in JM_type.items():
    if JM_type["J"] == JM_type["M"]:
        c = "J"
    elif max(JM_type.values()) == score_choices:
        c = type_survey

for type_survey, score_choices in AN_type.items():
    if AN_type["A"] == AN_type["N"]:
        d = "A"
    elif max(AN_type.values()) == score_choices:
        d = type_survey

answer = a + b + c + d
print(answer)