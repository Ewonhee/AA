
# import os
# import sys

# # 1. 현재 파이썬 파일이 있는 실제 폴더 위치를 자동으로 찾습니다.
# script_dir = os.path.dirname(os.path.realpath(__file__))

# # 2. 그 폴더 위치와 "input.txt"를 합쳐서 엽니다.
# sys.stdin = open(os.path.join(script_dir, "input.txt"), "rt")
# A = list(map(int, input().split()))

# print(A)



import sys
# sys.stdin=open("input.txt", "rt")
A = int(input())

for i in range(1, A+1):
    
    list_B = list(map(int, input().split()))
    list_C = list(map(int, input().split()))
    N=0
    s=0
    e=0
    k=0
    N = list_B[0]
    s = list_B[1]
    e = list_B[2]
    k = list_B[3]

    sliced_list = list_C[s-1:e]
    sliced_list.sort()
    awnser = sliced_list[k-1]
    print(f"#{i} {awnser}")
    

# for i in range(1, A+1):
#     n, s, e, k = map(int, input().split())
#     a=list(map(int, input().split()))
#     b=a[s-1:e]
#     b.sort()
#     awnser = b[k-1]
#     print(f"#{i} {awnser}")












