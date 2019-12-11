
arr = []

num = int(input("Enter the size of array : ")) 

for n in range (num):
    numbers = int(input("Input the no. in array : "))
    arr.append(numbers)
print ("Array = ",arr)

print("\nThe max no. = ", max(arr))
print("The min no. = ", min(arr))


# for already given array........

array2 = [10,35,56,65,345]
print("in array2 max no. is : ",max(ar))  # using in-bulit method max()
