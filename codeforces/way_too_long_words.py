n = int(input())
str_list = []

for _ in range(n):
    str_list.append(input())

for i in range(n):
    if len(str_list[i]) > 10:
        first = str_list[i][0]
        last = str_list[i][-1]
        middle = str(len(str_list[i]) - 2)
        str_list[i] = first + middle + last
    print(str_list[i])

# Codeforces 71A 문제 (Way Too Long Words)

# 단순한 구현 및 문자열 문제이다.
# 10보다 긴 문자열을 문제의 요구사항대로 줄이는 문제이다.
# indexing을 이용해서 맨 앞 문자와 뒷 문자를 들고오고
# 문자열의 길이에서 2를 빼주고 문자열 자료형으로 변환 시켜
# + 연산자를 이용해서 차례대로 붙여준다음 출력한다.
