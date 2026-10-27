import sys
# sys.stdin = open("in2.txt", 'rt')

n = int(input())
prime_list = list(map(int,input().split()))


def reverse(x):
    R_num=0
    # for i in range(len(x)):
    #     R_num = int(str(x)[::-1])
    R_num = int(str(x)[::-1])
    return R_num

def isPrime(x):
    if x<=1:
        return False
    for i in range(2, x):
        if x%i ==0:
            return False
    return True

R_rime_list=[]

# for i in range(len(prime_list)):
#     R_rime_num=int(str(prime_list[i])[::-1])
#     R_rime_list.append(R_rime_num)

# # print(R_rime_list)

# print(isPrime(23))
# print(isPrime(55))

# print(reverse(23))

for i in prime_list:
    num = reverse(i)
    R_rime_list.append(num)

# print(R_rime_list)

for j in R_rime_list:
    
    if isPrime(j) == True:
        print(j, end=' ')
    # else:
    #     print("소수가 없습니다.")

# print(reverse(12020))
