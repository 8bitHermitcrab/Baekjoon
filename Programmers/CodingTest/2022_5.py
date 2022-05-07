# rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# operations = ["Rotate", "ShiftRow"]

rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]


shift_count = 0
rotate_count = 0

for i in range(len(operations)):
    if operations[i] == "ShiftRow":
        shift_count += 1
    else:
        rotate_count += 1

# ShiftRow


# Rotate