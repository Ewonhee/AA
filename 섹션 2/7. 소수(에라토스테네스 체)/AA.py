import sys

# sys.stdin = open("input.txt",'rt')

n = int(input())

ch=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    # ch[0]은 소수
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1

print(cnt)




# # 1. 소수 판별 함수 (방금 수정했던 버전)
# def is_prime(x):
#     if x <= 1:
#         return False
        
#     for i in range(2, x):
#         if x % i == 0:
#             return False
            
#     return True

# # 2. 메인 로직
# N = 20
# count = 0  # 소수의 개수를 셀 변수

# print(f"{N}까지의 소수 목록:")

# for num in range(1, N + 1):
#     # num이 소수라면?
#     if is_prime(num):
#         print(num, end=" ")  # 가로로 출력
#         count += 1           # 개수 1 증가

# print(f"\n\n총 소수의 개수: {count}개")

