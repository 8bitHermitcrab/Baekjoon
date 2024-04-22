def solution(people, limit):
    people.sort()
    answer = 0
    i, j = 0, len(people)-1

    while i <= j:
        answer += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1

    return answer