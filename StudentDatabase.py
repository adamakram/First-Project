]Database=[]
dataBase=[]

def main():
    print("")
    print('Enter "A" to add a student')
    print('Enter "R" to remove a student')
    print('Enter "L" to list the database')
    print('Enter "G" to add a grade')
    print('Enter "X" to exit')
    print("")

    choice = input("Choose A, R, L or G (‘X’ for exit)")

    if choice == 'A':
        Add_Student()

    elif choice == 'R':
        Remove_Student()

    elif choice == 'L':
        List_Database()

    elif choice == 'X':
        Exit()

    elif choice == 'G':
        Grade()

    else:
        print('The option you entered is invalid, Please Try Again')
        main()




def sort(Database,L):
    print(L)
    L=L-1
    print(L)
    for i in range(L):
        for j in range(L-i-1):
            if Database[j][1]<Database[j+1][1]:
                x=Database[j+1]
                Database[j+1]=Database[j]
                Database[j]=x
                print(Database)
    return Database

def List_Database():
    listData=Database                 
    for i in range(len(Database)):
        if (len(listData[i]))==3:      
            x=listData[i].pop(1)
            y=listData[i].pop(1)
            z=x/y
            listData[i].append(z)
            print(listData)
        elif (len(listData[i]))==1:
            listData[i].append('None')
            print(listData)
            
    if (len(Database))== 0:
        print('')
        print('List Empty')
        main()
        
    elif (len(Database))>=2:
        count=0
        counter=0
        for i in range(len(Database)):
            while Database[i][1]==None:
                count+=1
                Database.append(Database[i])
                del Database[i]
                if count>len(Database):
                    break

        for j in range(len(Database)):
            if Database[j][1]==None:
                counter+=1


        L=(len(Database)-counter)
        Sorted=(sort(Database,L))

        for q in range(len(Sorted)):
            print(Sorted[q][0],'-GPA:', Sorted[q][1])
        main()
    else:
            print(Database[0][0],'-GPA:', Database[0][1])
            main()

        

def Add_Student():
  First_Name = str(input("New students' First name:"))
  while not First_Name.isalpha():
      print("Only letters are aloud!")
      First_Name = str(input("New students' First name:"))
      if First_Name.isalpha():
          break

  Surname = str(input("New students' Surname:"))
  while not Surname.isalpha():
      print("Only letters are aloud!")
      Surname = str(input("New students' Surname:"))
      if Surname.isalpha():
          break

  Full_Name = (First_Name + ' ' + Surname)
  Name = Surname + ' ' + First_Name

  if (len(Database)) > 0:
      nameCheck = [item[0] for item in Database]
      if Name in nameCheck:
          print('')
          print('Student', Full_Name, 'already exists')
          main()
      else:
          Database.append([Name])
          print('')
          print('Student', Full_Name, 'has been added')
          main()
  else:
      Database.append([Name])
      print('')
      print('Student', Full_Name, 'has been added')
      main()



      

      
def Remove_Student():
    First_Name = str(input('Existing students First name:'))
    while not First_Name.isalpha():
        print("Only letters are aloud!")
        First_Name = str(input('Existing students First name:'))
        if First_Name.isalpha():
            break
    Surname = str(input('Existing students Surname:'))
    while not Surname.isalpha():
        print("Only letters are aloud!")
        Surname = str(input('Existing students Surname:'))
        if Surname.isalpha():
            break

    Full_Name = (First_Name + ' ' + Surname)
    Name = (Surname + ' ' + First_Name)

    if(len(Database)) > 0:
        nameCheck = [item[0] for item in Database]
        if Name in nameCheck:
            x = (nameCheck.index(Name))
            del Database[(x)]
            print('')
            print('Student', Full_Name, 'deleted')
            main()
        else:
            print('')
            print('Student not in Database!')
            main()
    else:
        print('')
        print('Database empty!')
        main()





        
def Grade():
    First_Name = str(input('Existing students First name:'))
    while not First_Name.isalpha():
        print("Only letters are aloud!")
        First_Name = str(input('Existing students First name:'))
        if First_Name.isalpha():
            break

    Surname = str(input('Existing students Surname:'))
    while not Surname.isalpha():
        print("Only letters are aloud!")
        Surname = str(input('Existing students Surname:'))
        if Surname.isalpha():
            break

    Full_Name = (First_Name + ' ' + Surname)
    Name = (Surname + ' ' + First_Name)

    if (len(Database)) > 0:
        p = ([Database.index(i) for i in Database if (Name) in i])
        if p == []:
            print('Student is not in database!')
            main()
        else:
            Grades = ['', 'D', 'C', 'B', 'A']
            p = str(p)
            p = p.replace('[', '')
            p = p.replace(']', '')
            p = int(p)
            grade = input('Please enter a grade (A/B/C/D)')
            while grade not in Grades or grade == Grades[0]:
                print('Invalid Grade, try again')
                grade = input('Please enter a grade (A/B/C/D)')
                if grade in Grades and not grade == Grades[0]:
                    break
            while True:
                try:
                    Credit_Hours = float(input('Please enter credit hours (>0)'))
                except ValueError:
                    print("Not a Number! Try again.")
                    continue
                else:
                    break
            z = (Grades.index(grade))
            qualityPointstemp = round((Credit_Hours) * (z))
            print(qualityPointstemp, 'QPs added to', Surname,',',First_Name)
            dataBase = Database[p]
            if len(dataBase) < 2:
                dataBase.append(qualityPointstemp)
                dataBase.append(Credit_Hours)
                main()

# I ADDED FROM HERE...
##            for i in range(len(Database)):
##                if Database[i][1]==None:
##                    del Database[i][1]
##
##            for i in range(len(dataBase)):
##                if dataBase[i][1]==None:
##                    del dataBase[i][1]
#TO HERE            
            else:
                x = dataBase.pop(1)              #THUS SECTION IS CAUSING ISSUES...
                x = x + qualityPointstemp      #SHALL WE USE Database or dataBase when listing the database?
                y = dataBase.pop(1)
                y = y + Credit_Hours
                dataBase.append(x)
                dataBase.append(y)
                main()
    else:
        print('Database Empty!')
        main()

def Exit():
    print('Thank you - Goodbye.')


main()
