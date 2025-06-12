print("Enter a character : ", end="")
i = input()
if len(i) == 0:
    print("\nEnter a valid input!")
else:
    if i>="a" and i<="z":
        print("\n",i," is an alphabet.")
    elif i>='A' and i<='Z':
        print("\n",i," is an alphabet.")
    else:
        print("\n",i," is not an alphabet.")    