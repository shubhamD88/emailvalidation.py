email = input("Enter your Email : ");
k,j,d=0,0,0;
if len(email)>=6:# minimum length 6 caracter or more than that
    if email[0].isalpha():#start with alphabate 
        if ("@"in email) and (email.count("@")==1):# check is '@' in email id available and it was no reapeat.
            if  (email[-4]==".") ^ (email[-3]=="."):#dot position at index no. -4 or -3 ^ exor opretor use for only condition is true
                for i in email :
                    if i==i.isspace():#check is space available in email
                        k=1;
                    elif i.isalpha():#check i is alpha
                        if i==i.upper():
                            j=1;
                    elif i.isdigit():#verify is it digit
                        continue;
                    elif i=="_" or i=="." or i=="@":
                        continue;
                    else:
                        d=1;
                if k==1 or j==1 or d==1:
                    print("Wrong Email");
                else:
                    print("write Email");
            else:
                print("Wromg Email");
        else:
            print("Wromg Email");
    else:
        print(" Wrong Email");
else:
    print("Wrong Email ");
