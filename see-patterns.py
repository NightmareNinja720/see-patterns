#to show star pattern on lower left corner
ch='y'
while (ch=='y') or (ch=='Y'):
    b=int(input("Which shape pattern do you want?\n1.Rectangle's pattern\n2.Triangle's pattern\n3.Pyramid's pattern\nEnter serial no. of option which you want:"))
    if b==1:
        c=int(input("Which pattern do you want\n1.Rectangle star pattern\n2.Square pattern\nEnter serial no. of option which you want:"))
        if c==1:
            l=int(input("Enter length of rectangle:"))
            b=int(input("Enter breadth of rectangle:"))
            for i in range (l):
                for j in range (b):
                    print('*',end=' ')
                print()
        elif c==2:
            s=int(input("Enter side of the square:"))
            for i in range (s):
                for j in range (s):
                    print('*',end=' ')
                print()
        else:
            print("Invalid option")
    elif b==2:
        a=int(input("Which pattern do you want\n1.Lower left corner triangle\n2.Lower right corner triangle\n3.Upper left corner triangle\n4.Upper right corner triangle\nWriter serial no. of option for showing that pattern:"))
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
print("Hope u had fun")
