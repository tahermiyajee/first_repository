num=int(input("enter a number between 1-20"))
if num>20 or num<1:
    print("the number is gerater than 20 or less than 1 plz enter the number again")
else:
     with open(f"multiplication_table_of_{num}.txt", "a") as f:
          for i in range(1,11):
               print(num,'x',i,'=',num*i, file=f)

     
 

