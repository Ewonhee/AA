import sys

# sys.stdin = open("in1.txt", 'rt')



# int1, int2, int3 =map(int, input().split())

# print(f"{A} {int1} {int2} {int3}")
# 자릿수 구하는 함수
def digit_sum(X):
    total=0
    intsum = str(X)
    for i in range(len(intsum)):
        total+=int(intsum[i])

    # for i in str(x):

    return total

# 125를 10나눈몫으로 1+2+5한다.
# def digit_sum_2(X):
#     sum=0
#     while>0:
#         sum+=x%10 나머지
#         x=x//10 몫
#     return sum

# print(digit_sum(123))

A = int(input())
numbers = list(map(int, input().split()))

max_sum =-1
answer = 0
cnt=-1
# numbers 리스트로 num값
for idx, num in enumerate(numbers):
    current_num=digit_sum(num)

    if current_num > max_sum:
        max_sum=current_num
        answer=num
        cnt=idx

    # elif current_num == max_sum:
    #     max_sum == current_num
    #     answer = num
    #     cnt=idx



# print(numbers[cnt])
print(answer)


    
    
