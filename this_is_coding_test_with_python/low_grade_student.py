n = int(input())
ls = []

for _ in range(n):
    name, grade = input().split()
    ls.append((name, int(grade)))

def set(ls):
    return ls[1]

ls.sort(key = set)

for i in ls:
    print(i[0], end = ' ')

# 이것이 코딩테스트다 with Python 실전문제 6-11 문제 (성적이 낮은 순서로 학생 출력하기)
# P. 180

# 단순한 정렬문제인데 입력을 학생이름, 성적으로 받는다.
# 그리고 정렬을 성적이 낮은 순서대로 해야하는데
# 파이썬 기본 정렬 알고리즘을 이용해서 key 값을 주어서 성적을 기준으로
# 하게 해야한다.
# 위의 코드에서는 set이라는 함수를 따로 만들어줘서 적용시켜 주었는데
# lambda expression을 사용하면 더 간단하게 코드를 쓸 수 있다.
# ls.sort(key = lambda ls: ls[1]) 이렇게 작성이 가능하다.

# 더불어 입력을 문자열 형태인 학생이름과 정수형 형태인 성적을 공백으로
# 나눠서 받는데 반복문을 이용하여 리스트에 추가하는 방법을 잘 숙지하자!
