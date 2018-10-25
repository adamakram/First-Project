m = int(input('Please Enter The Minuites---'))  #User is asked to input minuites
m = m*60                                        #Program Converts minuites to seconds
s = float(input('Please Enter The Amount Of Seconds---'))  #Seonds are entred as a float

def SecondValidation(s):     #Subroutine for checking if valid seconds have been entered 
    if s>60 :               #Boolean Value of true or false is determined here
        print('Invalid')  
        s = float(input('Please Enter The Amount Of Seconds---'))     # User is asked to enter an appropriate value of seconds
        SecondValidation(s)    # Subroutine is called again if invalid seconds have been entered
    else:
        print('You Entered',# This statement prints the correct amount of seconds
          s , 'seconds')
        
def FinalSpeedCalculation(m,s):    # Subroutine used to calculate speed
    Total_Duration = m+s           # Duration of fall calculated in seconds
    Final_Speed= 9.8 * (Total_Duration)        # Final speed calculated in m/s
    Final_Speed= round(Final_Speed,2)          #Answer is rounded to a suitable figure
    Final_Speed_MPH= (3600*Final_Speed)/ 1609.34  # Final speed calculate in mph
    Final_Speed_MPH= round(Final_Speed_MPH,2)     #Answer is rounded to a suitable figure
    print(' The total duration of the fall is...', Total_Duration, 'seconds') #Duration of fall displayed
    print(' The final speed of the object is...', Final_Speed, 'm/s') #Speed of object in m/s displayed
    print(' or',Final_Speed_MPH , 'Miles Per Hour') #' Speed of object in mph displayed 
    

    
SecondValidation(s) # Subroutine called
FinalSpeedCalculation(m,s) # Subroutine called
