print('\t\t\t\t\tThe matrix calculator has been initiated.')
print()
r1=int(input('Enter the number of rows for matrix 1: '))        #no of rows are inputted here for matrix 1
c1=int(input('Enter the number of columns for matrix 1: '))     #no of rows are inputted here for matrix 1
r2=int(input('Enter the number of rows for matrix 2: '))        #no of rows are inputted here for matrix 2
c2=int(input('Enter the number of columns for matrix 2: '))     #no of rows are inputted here for matrix 2

                                                #THE FUNCTIONS:
    
def add(s,f):                               #the addition function
    '''The following function will add the matrices and return the final added result'''
    print('The answer is:')
    for i in range(len(s)):            #chooses the row of matrix 1
        for j in range(len(f[i])):     #chooses the column of matrix 2 (or inshort each value in row of matrix 1)
            add=int(s[i][j])+int(f[i][j])     
            print(add,sep='',end='   ')
        print()
          
def subtract(s,f):                         #the subtraction function
    '''The following function will subtract the matrices and return the final subtracted result'''
    print('The answer is:')
    for i in range(len(s)):           #chooses the row of matrix 1
        for j in range(len(f[i])):    #chooses the column of matrix 2 (or inshort each value in row of matrix 1)
            subtract=int(s[i][j])-int(f[i][j])
            print(subtract,sep='',end='   ')
        print()
          
def multiply(s,f):                        #the multiplication function 
    '''The following function will multiply the matrices and return the final multiplied result'''
    print('The answer is:')
    for i in range(len(s)):               #chooses the row of the first matrix
        for j in range(len(f[0])):        #chooses the column of the second matrix
            mult=0
            for k in range(len(f)):       #chooses the rows of the second matrix
                mult+=int(s[i][k])*int(f[k][j])
            print(mult,sep='',end='   ')
        print()       
        
def s_divide(s):                        #the scalar division function
    '''The following function will divide the matrix with a scalar quantity'''
    dividend=int(input('Enter integer you want the matrix to be divided with? '))   #user has the freedom to choose which scalar quantity to divide with
    print()
    print('The answer is:')
    for i in range(len(s)):          #choose the rows of the matrix
        for j in range(len(s[i])):   #choose the columns (or the single term from the row) of the matrix
            print(round((int(s[i][j])/dividend),1),end='   ')   #the answer is printed with one decimal place
        print()

def s_multiply(s):                   #the scalar multiplication function
    '''The following function will multiply the matrix with a scalar quantity'''
    mul=int(input('Enter integer you want the matrix to be multiplied with? '))  #user has the freedom to choose which scalar quantity to multiply with
    print() 
    print('The answer is:')
    for i in range(len(s)):            #choose the rows of the matrix
        for j in range(len(s[i])):     #choose the columns (or the single term from the row) of the matrix
            print(int(s[i][j])*mul,end='   ')
        print()
        
while True:
    flag=0
    Matrix1=[]
    Matrix2=[]   
    print()
    print('OPERATION MENU:')
    print()
    print('\t1. Addition')
    print('\t2. Subtraction')
    print('\t3. Multiplication')
    print('\t4. Scalar Division')
    print('\t5. Scalar Multiplication')
    print('\t6. Exit')
    print()
    n=int(input('Enter option number: '))
    print()

                                              #THE EXIT TO THE PROGRAM:
    
    if n==6:
        print('The program has been exited.')
        print()
        print('x'*100)
        break

                                               #THE MATRIX FORMATION:
    
    if True:
        for i in range(1,2):    #for matrix no. 1
            for j in range(1,r1+1):      #the number of rows needed      
               print('Enter values for matrix',i,'row',j,'separated by commas: ',end='')
               matrix1=input()             #user inputs the rows in this step
               Lmatrix1=matrix1.split(',')   #this method is used to eliminate ',' and to create a list
               Matrix1.append(Lmatrix1)      #appending the values in to the list
        if flag!=0:    #to break the loop if the input is incorrect according to the criteria input by the user
            break
        count=0
        for i in range(len(Matrix1)):
            for j in range(len(Matrix1[i])):
                count+=1   #counts the no. of values in the list
        if count==r1*c1:    #if the no. of values in the list meets the criteria
            pass
        else:
            print()
            print('Enter the right amount of values.')
            flag+=1
        
    if count==r1*c1:   #only operates if the first matrix is according to the criteria
        print()
        for i in range(2,3):    #for matrix no. 2
            for j in range(1,r2+1):          #the number of rows needed  
               print('Enter values for matrix',i,'row',j,'separated by commas: ',end='')
               matrix2=input()        #user inputs the rows in this step     
               Lmatrix2=matrix2.split(',')   #this method is used to eliminate ',' and to create a list
               Matrix2.append(Lmatrix2)     #appending the values in to the list
        if flag!=0:   #to break the loop if the input is incorrect according to the criteria input by the user
            break
        count=0
        for i in range(len(Matrix2)):
            for j in range(len(Matrix2[i])):
                count+=1    #counts the no. of values in the list
        if count==r2*c2:     #if the no. of values in the list meets the criteria
            pass
        else:
            print()
            print('Enter the right amount of values.')
            flag+=1
            

                                   #THE APPLICATION (OR THE CALLING) OF THE FUNCTION:
    
    if n==1 and flag==0:                     #for addition function
        if r1*c1==r2*c2:
            print()
            add(Matrix1,Matrix2)
        else:
            print()
            print('The no. of rows and columns in the first matrix does not match the no. of rows and columns in the second matrix')
          
    if n==2 and flag==0:                    #for subtraction function
        print()
        print('What do you want to do from the following given list?')
        print()
        print('1. Subtract Matrix 1 from Matrix 2')
        print('2. Subtract Matrix 2 from Matrix 1')
        print()
        subt=int(input('Choose: '))  #user has the freedom to choose which matrix to subtract which from
        if subt==1 and flag==0 and r1*c1==r2*c2:
            print()
            subtract(Matrix2,Matrix1)
        elif subt==2 and flag==0 and r1*c1==r2*c2:
            print()
            subtract(Matrix1,Matrix2)
        elif r1*c1!=r2*c2:
            print()
            print('The no. of rows and columns in the first matrix does not match the no. of rows and columns in the second matrix')

           
    if n==3 and flag==0:                   #for multiplication function
        print()
        print('What do you want to do from the following given list?')
        print()
        print('1. Multiply Matrix 1 with Matrix 2')
        print('2. Multiply Matrix 2 with Matrix 1')
        print()
        m=int(input('Choose: '))    #user has the freedom to choose which matrix to multiply which from
        if m==1 and c1==r2 and flag==0:
            print()
            multiply(Matrix1,Matrix2)
        elif m==2 and c2==r1 and flag==0:
            print()
            multiply(Matrix2,Matrix1)
        else:
            print()
            print('Multiplication is not possible.')


    if n==4 and flag==0:                   #for scalar division function
        print()
        print('What do you want to do from the following given list?')
        print()
        print('1. Divide Matrix 1 with a scalar quantity')
        print('2. Divide Matrix 2 with a scalar quantity')
        print()
        d=int(input('Choose: '))    #user has the freedom to choose which matrix to divide with a scalar quantity
        if d==1 and flag==0:
            print()
            s_divide(Matrix1)
        if d==2 and flag==0:
            print()
            s_divide(Matrix2)
            

    if n==5 and flag==0:               #for scalar multiplication function
        print()
        print('What do you want to do from the following given list?')
        print()
        print('1. Multiply Matrix 1 with a scalar quantity')
        print('2. Multiply Matrix 2 with a scalar quantity')
        print()
        mx=int(input('Choose: '))  #user has the freedom to choose which matrix to multiply with a scalar quantity
        if mx==1 and flag==0:
            print()
            s_multiply(Matrix1)
        if mx==2 and flag==0:
            print()
            s_multiply(Matrix2)       
