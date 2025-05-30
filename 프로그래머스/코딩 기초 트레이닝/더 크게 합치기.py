
# def solution(a, b):
#     answer = 0
#     if int(str(a)+str(b)) >= int(str(b)+str(a)) :
#         answer = int(str(a)+str(b))
#     else :
#         answer = int(str(b)+str(a))
#     return answer


# print(solution(123,4))

def solution(a, b):
    answer = 0
    if int(f'{a}{b}') >= int(f'{b}{a}') :
        answer = int(f'{a}{b}')
    else :
        answer = int(f'{b}{a}')
    return answer


# print(solution(123,123))
print(solution(123,4))