# 가장 가까운 같은 글자
def solution(s):
    answer = []
    s_dict = dict()

    for i in range(len(s)):
        # print(f's[{i}] = {s[i]}')
        if s[i] not in s_dict:
            answer.append(-1)
        else:
            answer.append(i - s_dict[s[i]])
        s_dict[s[i]] = i
        # print(f's_dict = {s_dict}')

    return answer

print(solution("banana"))

# 참고 : https://velog.io/@damin1025/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%EA%B0%80%EA%B9%8C%EC%9A%B4-%EA%B0%99%EC%9D%80-%EA%B8%80%EC%9E%90