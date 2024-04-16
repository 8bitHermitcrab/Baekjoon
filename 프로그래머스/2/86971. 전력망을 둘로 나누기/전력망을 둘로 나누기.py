def solution(n, wires):
    answer = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(i) for _ in sub for i in sub if set(i) & s]
        answer = min(answer, abs(2 * len(s) - n))
    return answer