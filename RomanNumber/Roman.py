d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,
        "XL":40,"XC":90,"CD":400,"CM":900}
s="III"
sum = 0
i=0
while i<len(s):
    temp=""
    if i == len(s)-1:
        temp=s[i]
    else:
        j=i+1
        temp = s[i]+s[j]
    if temp in d:
        sum = sum + d[temp]
        i+=2
    else: 
        sum = sum+d[s[i]]
        i+=1
print(sum)
