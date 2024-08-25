num=int(input("enter a number between 1-20"))
if num>20: 
    print("the number is gerater than 20 plz enter the number again")
else:
    for i in range(1,11):
        print(num,'x',i,'=',num*i)

