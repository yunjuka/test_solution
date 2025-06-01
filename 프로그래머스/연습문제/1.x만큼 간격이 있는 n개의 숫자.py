
def solution(x, n):
    answer = []
    for i in range(n) :
        answer.append(x*i)
    return answer

print(solution(-4,2))
print(solution(2,5))