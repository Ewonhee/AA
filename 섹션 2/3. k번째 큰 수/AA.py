import sys

# sys.stdin = open("intput.txt",'rt')

A, B = map(int, input().split())
list_c = list(map(int, input().split()))

final=0
# set() 중복된 값을 정리
list_sum= set()

for i in range(A):
    for j in range(i+1, A):
        for m in range(j+1, A):
            list_sum.add(list_c[i]+list_c[j]+list_c[m])
# set() sort 기능이없다
# print(list_sum)

anwser = list(list_sum)
anwser.sort(reverse=True)
final=anwser[B-1]

print(final)

