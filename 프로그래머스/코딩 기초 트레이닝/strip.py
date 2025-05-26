

# 파일 만들기 (예제용)
with open("example.txt", "w") as f:
    f.write("  Hello, world!  \n")

# 파일 읽고 strip() 적용
with open("example.txt", "r") as f:
    line = f.readline()
    print("원본:", repr(line))              # 줄바꿈과 공백 포함된 원본
    print("strip 후:", repr(line.strip()))  # 공백, 줄바꿈 제거됨
