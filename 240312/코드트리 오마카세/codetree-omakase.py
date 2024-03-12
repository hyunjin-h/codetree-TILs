l,q=map(int,input().split())

orders=[list(input().split()) for _ in range(q)]

belt=[{} for _ in range(l)] #[{key:value, key:value ...}, ...]
man=[['',0] for _ in range(l)]
now=0
for i in range(len(orders)):
    # print(i,end=' ')
    order=orders[i][0]
    t= int(orders[i][1])
    time=t-now
    now=t
    belt=belt[-time%l:]+belt[:-time%l]
    

    # 우선순위: 100->200->300
    if order=='100': # 초밥 만들기
        # 시각 t에 위치 x 앞에 name 부착한 초밥
        x=int(orders[i][2])
        name= orders[i][3]
        if name not in belt[x]:
            belt[x][name]=1
        else: 
            belt[x][name]+=1

    
    if order=='200': # 손님 입장
        # 이름이 name인 사람이 시각 t에 위치 x에 있는 의자
        # 자신의 이름과 같은거 n개 먹고 퇴장
        x=int(orders[i][2])
        name=orders[i][3]
        n=int(orders[i][4])
        man[x][0]=name
        man[x][1]=n

        
    

    for j in range(l):
            if len(belt[j])>0 and man[j][1]>0 and man[j][0] in belt[j]:
                man[j][1]-=belt[j][man[j][0]]
                belt[j][man[j][0]]=0
                del belt[j][man[j][0]]
                if man[j][1]<=0:
                    man[j][0]=''
        

    if order=='300':# 사진 촬영
        #사람 수와 남아 있는 초밥 수를 출력 
        people=0
        sushi=0
        for j in range(l):
            if man[j][0]!='':
                people+=1
            sushi+=sum(belt[j].values())
        print(people,sushi)