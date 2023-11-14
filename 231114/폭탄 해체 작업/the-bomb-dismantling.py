import heapq
n=int(input())
end_time=0
now_time=0
bombs=[]
for _ in range(n):
    score,time= map(int,input().split()) 
    end_time=max(end_time,time)
    bombs.append([score,time])
bombs=sorted(bombs,key=lambda x : (x[1],-x[0]))



score_board = []
for bomb in bombs:
    score,time = bomb
    if len(score_board) < time:
        heapq.heappush(score_board,score)
    else:
        before=heapq.heappop(score_board)
        heapq.heappush(score_board,max(score,before))

        
print(sum(score_board))