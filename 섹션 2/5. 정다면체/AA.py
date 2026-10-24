import sys

# sys.stdin=open("input.txt", "rt")

A, B = map(int,input().split())
# cnt 합리스트
cnt = [0]*(A+B+1)

for i in range(1, A+1):
    for j in range(1, B+1):
        # i+j 합이 나올때마다 cnt 리스트에 1씩 증가
        cnt[i+j]+=1

max_freq = max(cnt)

for i in range(len(cnt)):
    if cnt[i] == max_freq:
        print(i, end=' ')

# ----------------------------------------
# max= -123333

# for i in range(len(cnt)):
#     if cnt[i]>max:
#         max=cnt[i]

