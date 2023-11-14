import sys
n=int(input())
costs=list(map(int,input().split()))
min_cost=sys.maxsize
max_profit=0
for cost in costs:
    min_cost=min(min_cost,cost)
    max_profit=max(max_profit,cost-min_cost)

print(max_profit)