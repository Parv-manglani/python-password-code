



def check():
  a,b,c,d,e,f=0,0,0,0,0,0
  x=input("enter password: ")

  if len(x)>=10:
    a+=1

  for i in range(len(x)):
    if x[i]>="A" and x[i]<="Z":
       b+=1
  if b<2:
    print("The password must contain atleast 2 capital letters.")

  for i in range(len(x)):
    if x[i]>="a" and x[i]<="z":
      c+=1
  if c<2:
    print("The password must contain atleast 2 small letters.")

  for i in range(len(x)):
    if (x[i]>="1" and x[i]<="9") or x[i]==0 :
      d+=1
  if d<2:
    print("The password must contain atleast 2 digits.")
  for i in range(len(x)):
    if x[i]=="@" or x[i]=="#" or x[i]=="$" or x[i]=="%" or x[i]=="&" or x[i]=="*" or x[i]=="!":
      e+=1
  if e<2:
    print("The password must contain atleast 2 special characters.")


  for i in range(len(x)-3):
    if x[i]==x[i+1]==x[i+2]==x[i+3]:
      f+=1
  if f!=0:
    print("The password should not contain more than 3 characters consecutively.")

  if x==pass1 or x==pass2 or x==pass3:
    print("The password is not same as last 3 passwords.")

  if a!=0 and b>=2 and c>=2 and d>=2 and e>=2 and f==0 and x!=pass1 and x!=pass2 and x!=pass3 :
    print("password set successfully.")
  else:
    check()

username=input("enter username: ")
pass1=input("previous password1: ")
pass2=input("previous password2: ")
pass3=input("previous password3: ")
check()

