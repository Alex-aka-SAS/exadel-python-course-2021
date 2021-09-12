for k in range(1, 1000) :
    if(k>=1 and k<10):
        digit=k%10
        if digit**1==k:
         print ('Narcissistic__Number', k)
    if(k>=10 and k<100):
            digit1=k//10
            digit2= k%10
            if digit1**2+digit2**2==k:
                print ('Narcissistic__Number', k)
    if (k>=100 and k<1000):
                    digit3=k%10
                    digit4= k%100//10
                    digit5= k//100
                    if digit5**3+digit4**3+digit3**3==k:
                        print('Narcissistic__Number', k)