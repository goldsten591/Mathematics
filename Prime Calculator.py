user=input('>')

root=round((int(user))**0.5)
i=2

while  i <=  root:
    test=int(user)/i
    if test==int(test):
        print ("Not prime. Divisible by", i)
        break
    else:
        i+=1
    
print("Program complete")
