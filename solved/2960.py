from sys import stdin 

N,K = map(int,stdin.readline().strip().split())

def cnt(n,k):

    def era(n):
        t = [True]*(n+1)
        for i in range(2,int(n**0.5)+1):
            if t[i] == True:
                for j in range(i+i,n+1,i):
                    t[j] = False
        return [i for i in range(2,n+1) if t[i] == True]

    cnt = 0
    t2 = [True]*(n+1)
    for i in era(n):
        for j in range(i,n+1,i):
            if t2[j]==True:
                t2[j]=False
                cnt+=1
                if cnt == k:
                    return j

if __name__ == "__main__":
    print(cnt(N,K))