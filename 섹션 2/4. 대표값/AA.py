import sys

# sys.stdin=open("input.txt",'rt')

A=int(input())
list_B=list(map(int, input().split()))

list_B_sum=0
anwser =0

list_B_sum=sum(list_B)
avg = list_B_sum/A
# round() 함수는 소수점 첫째자리에서 반올림을 수행합니다.
avg=round(avg)

for i in range(len(list_B)):
    if avg == list_B[i]:
        anwser = list_B[i]
    else:
        anwser=min(list_B, key=lambda x: (abs(x-avg),-x))

for j in range(len(list_B)):
    if list_B[j] == anwser:
        final = j+1
        break

print(f"{avg} {final}")

# -----------------------------------------------
# ave=round(sum(a)/n)
# # idx 인덱스번호, x실제값
# min=2147000000
# for idx, x in enumerate(a):
#     # abs 절대값 x-ave로 평균과 실제값의 최소거리로 가까운 값을 찾는다.
#     tmp=abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x
#         res=idx+1
#     elif tmp == min:
#         if x>score:
#             score=x
#             res=idx+1

# print(ave, res)


# # -----------------------------------------------
# a=66.5
# a=a+0.5
# round는 round_half_even방식을 택한다. 그래서 0.5 더해주고
# a=int(a) 해줘야함