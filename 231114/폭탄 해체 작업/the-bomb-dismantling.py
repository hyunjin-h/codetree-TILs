n=int(input())
end_time=0
bomb=[]
for _ in range(n):
    score,time= map(int,input().split()) 
    end_time=max(end_time,time)
    bomb.append([score,time])

score_board=[0]*(end_time+1)
for i in range(n): 
    score_board[bomb[i][1]]=max(score_board[bomb[i][1]],bomb[i][0])

print(sum(score_board))