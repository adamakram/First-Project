
def SimplifyFraction(Num,Den):                             #Subroutine Called When The User Wants To Simplify The Fraction
    if Num==0 and Den==0 or Num==0:                        #When the following condition is met
        print('The result is zero')
        print('Goodbye')

    elif Den==0:                                           #When the Denominator is 0
        print('Result undetermined')
        print('Goodbye')
        
    else:
        while Den%2==0 and Num%2==0:                       #While the Denominator and Numerator are divisible by 2
            Num=Num//2                                     #Divide the numerator by 2
            Den=Den//2                                     #Divide the Denominator by 2
        while Num%3==0 and Den%3==0:                       #While the Denominator and Numerator are divisible by 3
            Num=Num//3                                     #Divide the numerator by 3
            Den=Den//3                                     #Divide the Denominator by 3
        while Num%5==0 and Den%5==0:                       #While the Denominator and Numerator are divisible by 5
            Num=Num//5                                     #Divide the numerator by 5
            Den=Den//5                                     #Divide the Denominator by 5
        while Num%7==0 and Den%7==0:                       #While the Denominator and Numerator are divisible by 7
            Num=Num//7                                     #Divide the numerator by 7
            Den=Den//7                                     #Divide the Denominator by 7
        while Num%11==0 and Den%11==0:                     #While the Denominator and Numerator are divisible by 11
            Num=Num//11                                    #Divide the numerator by 11
            Den=Den//11                                    #Divide the Denominator by 11

        if Num<0 and Den<0:                                #If both Numerator and Denominator are less than 0
            Num=Num*-1                                     #Multiply the Numerator by -1
            Den=Den*-1                                     #Multiply the Denominator by -1

        elif Num>0 and Den<0:                              #If the Numerator is greater than 0 and the Denominator is less than 0
            Num=Num*-1                                     #Multiply the Numerator by -1
            Den=Den*-1                                     #Multiply the Denominator by -1
  
        print('The simplified fraction is', Num,'/',Den)   #Display the Simplified Fraction
        print('Goodbye')


def UserInput():                                           #Subroutine to check the User Input
    
    NumCheck = float(input('Please Enter The Numerator'))  #Imput field which takes in floats
    Num= int(NumCheck)                                     #An integer version of the float is defined
    if NumCheck==Num:                                      #If the integer version of the float matches the imput
        print('')                                          #The program continues
    else:
        print('__________________________________')        #Validation Message displayed
        print('Please enter only integer numbers')
        print('__________________________________')
        UserInput()

    DenCheck = float(input('Please Enter The Denominator'))#Imput field which takes in floats
    Den= int(DenCheck)                                     #An integer version of the float is defined
    if DenCheck==Den:                                      #If the integer version of the float matches the imput
        print('')                                          #The program continues
    else:
        print('__________________________________')
        print('Please enter only integer numbers')
        print('__________________________________')        #Validation Message displayed
        UserInput()

    
    print("The Fraction is..",Num,'/',Den)                 #The simplified fraction is displayed 
    Ans= str(input('Press Enter To Simplify The Fraction'))
    SimplifyFraction(Num,Den)                              #The subroutine is called at the end of all the validations


UserInput()                                                #This subroutine is called when the program is run                             
