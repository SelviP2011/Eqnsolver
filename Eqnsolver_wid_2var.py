#Eqn solver with two unknown variable
def xy(a):
    h=""
    for i in a:
        if i=="x":
            if(h in "+-"):    h+="1"
            t=int(h);h=""
        elif i=="y":
            if(h in "+-"):    h+="1"
            g=int(h);h=""
        else:
            h+=i
    y=int(h[1:])
    return t,g,(-1*y)
a=str(input().strip())
b=str(input().strip())
c,d,e=xy(a);x,y,z=xy(b)
print(int(((d*z)-(y*e))/((c*y)-(x*d))))
print(int(((e*x)-(z*c))/((c*y)-(x*d))))

    
