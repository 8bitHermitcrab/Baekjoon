''' 오답정리 '''

def solution(array, commands):

    answer = []

    for command in commands:
        new_array = array[command[0]-1:command[1]] # 문제에서 주어진 크기만큼 자르기
        new_array.sort() # sort 함수로 정렬
        answer.append(new_array[command[2]-1]) # k 번째 값 집어넣기

    return answer

'''
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. 
[2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. 
[6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. 
[1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.

array = [1, 5, 2, 6, 3, 7, 4]
answer = []

array1 = array[1:5].sort()
print(f'array1 = {array1}')

array3 = array.sort()
c = array3[2]
print(f'c = {c}')
answer.append(c)
print(answer)

https://sinsomi.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-K%EB%B2%88%EC%A7%B8%EC%88%98
'''