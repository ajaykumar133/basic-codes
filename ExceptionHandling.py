class EH:

    def mtd(s):
        if __name__ == "__main__":               #this will lead to stop running of code-parameters inside this block when accessed by another py file as-
            print("\n Input no. you want to Divide. \n")              #   - by practice3
            a = float(input("enter 1st no. :"))
            b = float(input("enter 2nd no. :"))

            try:
                c = a / b
                print("\n Division = ", c)
            except:
                print("You can't divide by zero .")
            else:
                print("\n division completed .")
            finally:
                print("sucessfully ended.")

    def add(x,y):
        return x+y
    if __name__=="__main__":
        print(add(10,16))

obj = EH()
obj.mtd()