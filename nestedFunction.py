class nested_fn:

    def outfn(text):
        def infn():
            print(2+6)

        infn()                      # this is to call the inner_function , and execute the code inside those inner_function
        print(3+1)

    def out1(self):
        print('this is 1')
        a=1
        b=2
        def out2():
            print('this is 2')
            c=a+b
            print(a+b)
            def out3():
                print('this is 3')
                print(c+a)
                def out4():
                    print('this is 4')

                    def out5():
                        print('this is 5')

                        def out6():
                            print('this is 6')

                            def out7():
                                print('this is 7')

                                def out8():
                                    print('this is 8')

                                    def out9():
                                        print('this is 9')

                                        def out10():
                                            print('this is 10')
                                            print(c+b)

                                        out10()
                                    out9()
                                out8()
                            out7()
                        out6()
                    out5()
                out4()
            out3()
        out2()

nf=nested_fn()
nf.outfn()
nf.out1()