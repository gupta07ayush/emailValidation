#Email validation in python using string Functions

email = input("Enter your Email id: ") 

#g@g.in  : This the smallest string as email id ever existed.(6 characters)
k,j,d=0,0,0
if len(email)>=6: #1
    if email[0].isalpha():  #2
        if ('@' in email) and (email.count("@")==1):  #3
            if (email[-4]=='.') ^ (email[-3]=='.'):   #4
                for i in email:
                    if i==i.isspace():  #5
                       k=1
                    elif  i.isalpha():
                        if i==i.upper():  #5
                            j=1   
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@" or i=="+":
                        continue
                    else: #5
                        d=1
                if k==1 or j==1 or d==1: 
                    print("Wrong Email 5 (There should be no space in your email id and put email id in lower case)")   
                else:
                    print("Right Email")
            else:
                print("wrong Email 4 ( . is misplaced)") 
        else:
            print("Wrong Email 3 (There should be exact one @ )")
    else:
        print("Wrong Email 2 (should starts with an alphabet)")
else:
    print("Wrong Email 1 (too small)")



