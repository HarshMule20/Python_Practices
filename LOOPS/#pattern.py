i=1                             #initializing
while (i<=5):                   #giving condition in while loop
    j=1                         #initializing
    while(j<=5):                #somewhat nested while
        print("#",end="")       #printing the value
        j=j+1                   #incrementing the variable of inner loop
    i=i+1                       #incrementing the variable of outer loop
    print()                     #to change a line after each loop
