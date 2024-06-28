import statistics

def get_numbers():

    while True:
      try:
            num1 =float(input("enter the first number"))
            num2 =float(input('enter the second number'))
            return(num1,num2)
      except ValueError:
          print('invalid input.please enter numbers only')
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return(num1*num2)

def division(num1,num2):
    if num2==0:
        print('Error:cannot divide by zero')
        return None
    return(num1/num2)
def calculate(numbers,operation):

    if operation =='+':
        return add(numbers[0],numbers[1])
    elif operation =='-':
        return subtract(numbers[0],numbers[1])
    elif operation =='*':
        return multiply(numbers[0], numbers[1])
    elif operation =='/':
        return division(numbers[0],numbers[1])
    else:
        print('invalid operation symbol')
        return None
def statistics_calculator(data):
# calculate various statitics by the list of data

  print('Mean:',statistics.mean(data))
  print('Median:',statistics.median(data))
  print('mode:',statistics.mode(data))
  print('minimum:',min(data))
  print('maximum:',max(data))
  print('variance:',statistics.variance(data))
  print('standard Deviation:',statistics.stdev(data))
  
def main():
    #the main function that drives the calculator program.
    while True:
        print("\n-----calculator-----")
        print('1.Arithmatic Operations')
        print("2.Statistical function")
        print("3.Exit")
        choice=input('Enter your chhoice (1-3)')
        if choice=='1':
         numbers=get_numbers()
         operation =input('Enter operation(+,-,*,/):')
         result =calculate(numbers,operation)
         if result is not None:
             print('result',result)

        elif choice=='2':
            data =[]
            while True:
                num =input("'Enter a number(or 'q'to quit):")
                if num=='q':
                  break
                try:
                    data.append(float(num))  
                except ValueError:
                    print('invalid input.please enter numbers only')
            if data:
                statistics_calculator(data)

        elif choice==3:
            break
        else:
            print('invalid choice.please try again')
if __name__== "__main__":
    main()

#    https://github.com/satyaumi/statistics-calculator.git