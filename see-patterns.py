#to show star pattern on lower left corner
ch='y'
while (ch=='y') or (ch=='Y'):
    b=int(input("which shape pattern do you want\n1.rectangle's pattern\n2.triangle's pattern\n3.pyramid's pattern\nEnter serial no. of option which you want:"))
    if b==1:
        c=int(input("which pattern do you want\n1.rectangle star pattern\n2.square pattern\nEnter serial no. of option which you want:"))
        if c==1:
            l=int(input("enter length of rectangle:"))
            b=int(input("enter breadth of rectangle:"))
            for i in range (l):
                for j in range (b):
                    print('*',end=' ')
                print()
        elif c==2:
            s=int(input("enter side of the square:"))
            for i in range (s):
                for j in range (s):
                    print('*',end=' ')
                print()
        else:
            print("invalid option")
    elif b==2:
        a=int(input("which pattern do you want\n1.Lower left corner triangle\n2.Lower right corner triangle\n3.upper left corner triangle\n4.upper right corner triangle\nwriter serial no. of option for showing that pattern:"))
        h=int(input("Enter height of the triangle:"))
        if a==1:
            for i in range (h+1):
                for j in range (i):
                    print('*',end=' ')
                print()
        elif a==2:
            for i in range (h+1):
                for j in range (h-i):
                    print(' ',end=' ')
                for k in range (i):
                    print('*',end=' ')
                print()
        elif a==3:
            for i in range (h+1):
                for j in range (h-i):
                    print('*',end=' ')
                print()
        elif a==4:
            for i in range (h+1):
                for j in range (i):
                    print(' ',end=' ')
                for k in range (h-i):
                    print('*',end=' ')
                print()
        else:
            print("Invalid option")
    #elif b==3:
    ch=input("Do you want to see more patterns:")
print("Goodbye")
print("hope u had fun")
