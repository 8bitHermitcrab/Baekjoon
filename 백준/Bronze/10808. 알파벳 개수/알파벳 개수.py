word = input()

alpabat = [0] * 26

for i in range(len(word)):

    if word[i] == 'a':
        alpabat[0] += 1

    elif word[i] == 'b':
        alpabat[1] += 1

    elif word[i] == 'c':
        alpabat[2] += 1

    elif word[i] == 'd':
        alpabat[3] += 1

    elif word[i] == 'e':
        alpabat[4] += 1

    elif word[i] == 'f':
        alpabat[5] += 1

    elif word[i] == 'g':
        alpabat[6] += 1

    elif word[i] == 'h':
        alpabat[7] += 1

    elif word[i] == 'i':
        alpabat[8] += 1

    elif word[i] == 'j':
        alpabat[9] += 1

    elif word[i] == 'k':
        alpabat[10] += 1

    elif word[i] == 'l':
        alpabat[11] += 1

    elif word[i] == 'm':
        alpabat[12] += 1

    elif word[i] == 'n':
        alpabat[13] += 1

    elif word[i] == 'o':
        alpabat[14] += 1

    elif word[i] == 'p':
        alpabat[15] += 1

    elif word[i] == 'q':
        alpabat[16] += 1
        
    elif word[i] == 'r':
        alpabat[17] += 1

    elif word[i] == 's':
        alpabat[18] += 1

    elif word[i] == 't':
        alpabat[19] += 1

    elif word[i] == 'u':
        alpabat[20] += 1

    elif word[i] == 'v':
        alpabat[21] += 1

    elif word[i] == 'w':
        alpabat[22] += 1

    elif word[i] == 'x':
        alpabat[23] += 1

    elif word[i] == 'y':
        alpabat[24] += 1
        
    elif word[i] == 'z':
        alpabat[25] += 1

print(*alpabat)