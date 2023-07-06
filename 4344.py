C = int(input())

data = []
average = []
rate = []

for i in range(C):
  data.append(list(map(float,input().split())))

for i in data:
  average.append(sum(i[1:])/i[0])

for i in range(len(data)):

  for j in range(len(data[i])-1):
    if data[i][j+1] > average[i]:
      data[i][j+1] = 1
    else:
      data[i][j+1] = 0
  
  rate.append(sum(data[i][1:])/data[i][0])

for i in rate:
  print(f"{round(i*100,3):.3f}%")

