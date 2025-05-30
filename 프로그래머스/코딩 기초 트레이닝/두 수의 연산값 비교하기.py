
# def solution(a, b):
#     answer = 0
#     if int(f'{a}{b}') >= 2*a*b :
#         answer = int(f'{a}{b}')
#     else :
#         answer = 2*a*b
#     return answer

def solution(a, b):
    return(max(int(f'{a}{b}'),2*a*b))

print(solution(2,91))