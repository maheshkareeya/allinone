# input()
# line1 = set(map(str,input().split()))
# input()
# line2 = set(map(str,input().split()))
# print(len(list(line1.intersection(line2))))
# input()
# line1 = set(map(str,input().split()))
# input()
# print(len(list(line1.intersection(set(map(str,input().split()))))))

_, a = input(), set(input().split())
_, b = input(), set(input().split())
print(len(a.intersection(b)))

# _, a = input(), set(input().split())
# _, b = input(), set(input().split())
# line = a.intersection(b)
# print(*line)
