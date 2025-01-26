from sys import stdin   
import decimal

N = int(stdin.readline().strip())

credit = {
"A+": '4.3', 
"A0": '4.0', 
"A-": '3.7',
"B+": '3.3', 
"B0": '3.0', 
"B-": '2.7',
"C+": '2.3', 
"C0": '2.0', 
"C-": '1.7',
"D+": '1.3', 
"D0": '1.0', 
"D-": '0.7',
"F":  '0.0'
}
total_score,total_credit = 0,0

for _ in range(N):
    _,score,grade = stdin.readline().strip().split()
    total_score+=int(score)
    total_credit+=decimal.Decimal(credit[grade])*int(score)

print(round(total_credit/total_score,2))
