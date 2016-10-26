#reverse hash problem

def reverseHash(n,letters):
    if n==0:
        return None
    elif n>0 and n<259:
        return None
    elif n>=259:
        str,str1="",""
        rem=n%37
        n=n/37     
        if n!=7 and n/37==0:
            return None
        else:
            while (n*37)+rem>=259:
                if rem<len(letters):
                    str=str+letters[rem]
                    rem=n%37
                    n=n/37
                else:
                    break
            if len(str)>0:
                j=len(str)-1
                while j>=0:
                    str1=str1+str[j]
                    j-=1
                return str1
            else:
                return None
        
    
    
#main driver code

n=raw_input("Enter your hash code value ")
hash=int(n)
letters="acdegilmnoprstuw" #this can be taken as input from user also
str=reverseHash(hash,letters)
if str is not None:
    print "The required string is ",str  
else:
    print "The hash code is not correct"
