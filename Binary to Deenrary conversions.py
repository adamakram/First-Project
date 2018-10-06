
def BinaryToDecimal():
    binary = input('[Please Enter A Binary Number To Be Converted]')
    decimal=0
    for digit in binary:
        decimal = decimal*2 + int(digit)
        print(decimal)
    print("______________________________________________________")
    MainMENU()

def ConvertDecimalToBinary():
    print("Please Enter A Number To Be Converted")
    BinaryList = [ 128, 64, 32, 16, 8, 4, 2, 1]
    DecimalInput =int(input())
    BinaryOutput= []
    for i in BinaryList:
        if DecimalInput>= i :
            DecimalInput -=i
            BinaryOutput.append(1)
        else:
            BinaryOutput.append(0)
    print(BinaryOutput)
    print("______________________________________________________")
    MainMENU()

    
def BinaryAddition():
    print("")
    binary1 = input('Please Enter your first Binary number')
    binary2 = input('Please Enter your Secuond Binary number')
    Answer=0
    decimal1=0
    for digit in binary1:
        decimal1 = decimal1*2 + int(digit)
    decimal2=0
    for digit in binary1:
        decimal2 = decimal2*2 + int(digit)
    Answer=decimal1+decimal2
    print("")
    BinaryList = [ 128, 64, 32, 16, 8, 4, 2, 1]
    BinaryOutput= []
    for i in BinaryList:
        if Answer>= i :
            Answer -=i
            BinaryOutput.append(1)
        else:
            BinaryOutput.append(0)
        print(BinaryOutput)
    print("______________________________________________________")
    MainMENU()

def BinaryMultiplication():
    print("")
    binary1 = input('Please Enter your first Binary number')
    binary2 = input('Please Enter your Secuond Binary number')
    Answer=0
    decimal1=0
    for digit in binary1:
        decimal1 = decimal1*2 + int(digit)
    decimal2=0
    for digit in binary1:
        decimal2 = decimal2*2 + int(digit)
    Answer=decimal1*decimal2
    print("")
    BinaryList = [ 128, 64, 32, 16, 8, 4, 2, 1]
    BinaryOutput= []
    for i in BinaryList:
        if Answer>= i :
            Answer -=i
            BinaryOutput.append(1)
        else:
            BinaryOutput.append(0)
        print(BinaryOutput)
    print("______________________________________________________")
    MainMENU()
    

def MainMENU():
    print("[-MAIN MENU-]")
    print("")
    print("[Enter 1 for binary to decimal]")
    print("")
    print("[Enter 2 for decimal to Binary]")
    print("")
    print("[Enter 3 To add together two binary niumbers]")
    print("")
    print("[Enter 4 to multiply two binary numbers]")
    print("")

    MenuOption= int(input("Please enter a Choice--"))

    if MenuOption>4:
        print("That Is Not A Valid Option- Please try again")
        MainMENU()

    if MenuOption == 1:
        BinaryToDecimal()
    elif MenuOption == 2:
        ConvertDecimalToBinary()
    elif MenuOption== 3:
        BinaryAddition()
    elif MenuOption==4:
        BinaryMultiplication()
        
MainMENU()


