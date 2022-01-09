#에라토스테네스의 체 활용
m, n = map(int, input().split())

def isPrime(m, n):
    n += 1
    prime = [True] * n  # n개의 [True]가 있는 리스트 생성
    for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사
        if prime[i]:
            for j in range(2*i, n, i):
                prime[j] = False
    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)
isPrime(m, n)
