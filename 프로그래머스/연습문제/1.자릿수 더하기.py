
def solution(n):
    answer = []
    a = list(map(int,str(n)))
    for i in range(n,0,-1):
        answer.append(a[i])
    return answer

print(solution(12345))