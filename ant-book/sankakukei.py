# 三角形の成立条件はある辺aが残りの辺の足し算b+cよりも短い（これはすべての辺で同様）
N = int(input())
A = list(map(int, input().split()))
cnt = 0
res = 0

for a in A:
    for b in A:
        for c in A:
            triangle = [a, b, c]
            triangle.sort(reverse=True)
            if triangle[0] < triangle[1] + triangle[2] and sum(triangle) > res:
                res = sum(triangle)
                cnt += 1

if cnt == 0:
    print(0)
else:
    print(res)
