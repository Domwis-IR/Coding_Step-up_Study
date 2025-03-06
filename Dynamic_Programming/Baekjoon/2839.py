# 5kg 봉지와 3kg 봉지의 최소 개수를 구하는 문제
# 5kg 봉지를 최대한 많이 사용해야 한다.
# 5kg 봉지를 최대한 많이 사용하되, 3kg 봉지를 사용할 수 없는 경우 -1을 출력한다.

N = int(input())
bags = 0

while N >= 0:
    if N % 5 == 0:  # If N is divisible by 5
        bags += N // 5
        print(bags)
        break
    N -= 3
    bags += 1
else:
    print(-1)