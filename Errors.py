# ERROR HANDLING

while True:
    try:
        age= int(input('Enter your age: '))
        print(age)
        print('thanks')
        break
    except:
        print('Please enter the number')
        

while True:
    try:
        age= int(input('Enter your age: '))
        print(age)
    except:
        print('Please enter the number')
    else:
        print('thanks')
        break
    

def division(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as err: # Error Wrapping
        print(err)
        

print(division(1,'1'))
print(division(1,0))

while True:
    try:
        age= int(input('Enter your age: '))
        print(5/age)
    except ValueError:
        print('Please enter the number')
    except ZeroDivisionError:
        print('Provide number greater than Zero')
    else:
        print('thanks')
        break
    finally: # it runs regardless of anything.
        print('End')
        
        
while True:
    try:
        age= int(input('Enter your age: '))
        print(5/age)
    except ValueError:
        print('Please enter the number')
        continue
    except ZeroDivisionError:
        print('Provide number greater than Zero')
        break
    else:
        print('thanks')
    finally:
        print('End')      
    print('Move On')  
        

while True:
    try:
        age= int(input('Enter your age: '))
        print(5/age)
        raise ValueError('Stop Now')
    except ZeroDivisionError:
        print('Provide number greater than Zero')
    else:
        print('thanks')
        break
    finally:
        print('End')
        
        

        