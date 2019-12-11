#=============== to check if a year is leap year or not  ============================#

year = int(input("enter the year you want to check :"))

print("year = ",year)

if (year%4==0) :
    print("Yes, year",year,"it is a leap year")
else:
    print(year," is not leap year ")

# ============== TO CHECK IF ELEMENT EXIST IN THE GIVEN LIST ========================#


list=['hlo','ye','gh','ab']

if 'ab' in list:
    print("\n\n yes the element exist in list .")
else:
    print("no the element exist in list .")

#=============== string concatination ============================================#

str1= input("enter 1st str : ")
str2= input("enter 2nd str : ")
strctn=str1+str2
print(strctn)
