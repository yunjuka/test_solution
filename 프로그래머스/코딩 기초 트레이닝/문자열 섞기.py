
# def solution(str1, str2):
#     answer = ""
#     for a, b in zip(str1, str2):
#         answer += a + b
#     return answer

def solution(str1, str2) :
    answer = ''
    for i in range(len(str1)) :
        answer += str1[i] + str2[i]
    return answer
    

print(solution('aaaa','bbbb'))