import time
def P11():
    diff_file = open('NewtonFIF.txt', 'w')
    diff_file.close()


    # deliberately not importing math.
    def factorialfunc(n):
        '''
        Returns the factorial of a positive integer.
        '''
        assert type(n) == type(1) or type(n) == type(1.0), "n is not a number."
        n = int(n)
        assert n > 0, "Can not find factorial of a negative number."
        if n == 1:
            return 1
        else:
            return n * factorialfunc(n-1)


    def diffgen(diff_file):
        '''
        Finds the first, second, third (and so on) difference of given y values.
        '''
        print('\nCreating difference table for difference 1')
        # time.sleep is used to make output on terminal more pleasant
        time.sleep(1)
        diff_file = open('NewtonFIF.txt', 'r')
        filevals = list(diff_file.readlines()[-1].split())
        diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
        # prints diffvals
        for val in diffvals:
            print(val)
        diff_file = open('NewtonFIF.txt', 'a')
        diff_file.writelines([" ".join(str(val) for val in diffvals)])
        diff_file.write('\n')
        iternum = len(filevals) - 2  # 1 because it has been done above
        for i in range(iternum):
            print('\nCreating difference table for difference {}'.format(i+2))
            time.sleep(1)
            diff_file = open('NewtonFIF.txt', 'r')
            filevals = list(diff_file.readlines()[-1].split())
            diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
            # prints diffvals
            for val in diffvals:
                print(val)
            diff_file = open('NewtonFIF.txt', 'a')
            diff_file.writelines([" ".join(str(val) for val in diffvals)])
            diff_file.write('\n')
            diff_file.close()
        print('\n')


    def genpterm(p, iternum, y0terms):
        '''
        Generates the value of p term for terms in the main equation.
        '''
        pterm = 1
        print('\nCalculating pterm of {} term'.format(iternum + 2))
        for i in range(iternum+1):
            print('\tpterm = {} * ({} - {})'.format(pterm, p, i))
            pterm *= p - i
            print('\tpterm is {}'.format(pterm))
        return pterm


    def ypgen(diff_file, p):
        '''
        Calculates value of yp by finding and adding all the terms.
        '''
        diff_file = open('NewtonFIF.txt', 'r')
        content = diff_file.readlines()
        y0terms = []
        for i in content:
            y0terms.append(i.split()[0])
        y0terms = [float(term) for term in y0terms]
        yp = y0terms[0]
        y0terms = y0terms[1:]
        iternum = len(y0terms)
        print('\nAs p = {}'.format(p))
        for i in range(iternum):
            print("\n")
            print('{} term of yp is (pterm * {}) / {}!'.format(i + 2, y0terms[i], i + 1))
            time.sleep(1)
            yp += float(genpterm(p, i, y0terms) * y0terms[i]) / float(factorialfunc(i+1))
        print('returning yp = {}'.format(yp))
        diff_file.close()
        return yp



    print("What is the number of values of x?")
    n = int(input())
    print('\n')
    h = input('Are the values equally spaced?\nIf yes enter value of \'h\'. If no, press \'n\': ')
    if h == 'n':
        print("Newton's Forward Interpolation Formula can not be applied.\nExiting program.")
        exit()
    else:
        try:
            h = float(h)
        except:
            h = input('Please enter a valid number for h. ')
            while type(h) != type(1.0) and type(h) != type(1):
                h = input('Please enter a valid number for h. ')
                try:
                    h = float(h)
                except:
                    pass
    x0 = float(input('Enter value of x0. '))
    xvals = [(x0 + (i * h)) for i in range(n)]
    print("The values of x are: ")
    for i in xvals:
        print(i),
    print('\n')
    xp = float(input('Enter the value of xp. '))
    print("Finding the value of p.")
    print("Using the formula xp = x0 + ph")
    print("Here {} = {} + p * {}".format(xp, x0, h))
    p = (float(xp - x0)) / float(h)
    print('Value of p is: {}'.format(p))
    print('Values of x are ', xvals)
    yvals = [None] * n
    for i in range(n):
        ytemp = float(input('Enter value of y{}: '.format(i)))
        yvals[i] = ytemp
    with open('NewtonFIF.txt', 'a') as diff_file:
        diff_file.write(' '.join([str(val) for val in yvals]))
        diff_file.write('\n')
    print('\nValues of y are {}'.format(yvals))
    xtoymap = {}
    for i in range(n):
        xtoymap[xvals[i]] = yvals[i]
    print('\nx values & corresponding y values are:')
    print('\nx values            y values')
    for key in xtoymap:
        print('\n{}                 {}'.format(key, xtoymap[key]))
    diff_file = open('NewtonFIF.txt', 'a')
    diffgen(diff_file)
    diff_file.close()
    yp = ypgen(diff_file, p)
    decimalval = int(input('\n\nHow many decimal digits accuracy do you want\nfor the value of yp = y({}): '.format(xp)))
    yp = round(yp, decimalval)
    print('Value of yp = y({}) = {}'.format(xp, yp))

