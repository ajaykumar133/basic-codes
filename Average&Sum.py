class maths:

    def average(self):
        print('=========================== THIS WILL GIVE AVERAGE OF NO. ====================')

        a=[]
        limit=int(input('enter the size how much no.s you want to input :'))

        for i in range(1,limit+1):
            n=int(input('enter the no %d :'%i))

            a.append(n)

        print(a)
        sum_of_list=sum(a)
        print('sum =',sum_of_list)

        avg= sum_of_list / (limit+1)
        print('average of the entered no. is :',avg)

    def sum(self):
        print('==============  THIS WILL PRINT THE SUM OF 1ST n NATURAL NO. ==============')

        max_no = int(input('enter the no. upto which you want to sum-up the numbers :'))
        sum=0
        for i in range(1,max_no+1):
            sum=sum+i

        print('sum of 1st',max_no,'no. is = ',sum)

mt=maths()
mt.average()
#mt.sum()
