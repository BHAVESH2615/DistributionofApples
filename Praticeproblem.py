def Apple(no,min1,max1):
    if min1 > no:
        print(f"Enter the Minumum NUmber which should be smaller than  0 - {no - 1}")
        exit()
    if max1 > no or max1 < min1:
        print(f"Enter the Maximum NUmber which should be smaller than  0 - {no - 1} and greater than {min1}")
        exit()
    if min1==max1:
        print("Both Number should not be Same")
        exit()

    for i in range(min1,max1+1):
        if no%i==0:
            print(f"{i} divisor of   {no} ")
        else:
            print(f"{i} not a divisor of   {no} ")


if __name__ == '__main__':
    while True:
        try:
            no = int(input("enter the number of Apples:- "))
            min1 = int(input(f"Enter the Minumum NUmber which should be smaller than  0 - {no-1} :- "))
            max1 = int(input(f"Enter the Maximum NUmber which should be smaller than  0 - {no - 1} and greater than {min1} :- "))
            Apple(no,min1,max1)
        except ValueError:
            print("Enter Integers Only.....")

