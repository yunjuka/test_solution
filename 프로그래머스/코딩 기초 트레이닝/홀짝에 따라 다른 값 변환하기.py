
#짝수일 때 1부터 n까지 %2==0 이면 += 아니면 넘어감

def solution(n):
    answer = 0
    if n % 2 == 0 :
        for i in range(1,n+1):
            if i % 2 == 0:
                answer += i*i
            else:
                answer = answer
    else:
        for i in range(1,n+1):
            if i % 2 != 0:
                answer += i
            else:
                answer = answer
    return answer

print(solution(10))