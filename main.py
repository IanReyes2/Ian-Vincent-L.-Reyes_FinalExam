def main():
    # Find the least number among three numbers

    L = []
    txtfld1 = eval(input("Enter the first number:"))
    L.append(txtfld1)
    txtfld1.place(x=80, y=150)
    txtfld2 = eval(input("Enter the first number:"))
    L.append(txtfld2)
    txtfld2.place(x=80, y=150)
    txtfld3 = eval(input("Enter the first number:"))
    L.append(txtfld3)
    txtfld3.place(x=80, y=150)

    print("The smallest number among the three is:",str(min(L)))
main()