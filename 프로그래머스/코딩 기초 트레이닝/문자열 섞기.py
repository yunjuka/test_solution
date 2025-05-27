
a = input()
b = input()

 
# a의 짝수 번째 번호를 b의 짝수번호와 바꿈
# i는 a부터 

for i in range(len(a)) :
    a.replace(a[i%2==0],b[i%2==0])

print(a)