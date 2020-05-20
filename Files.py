maintextinstarting = '''This is the testing file for FilesIO.
:)
The line written for readline(s).'''

myfile = open('Test.txt') # Can only read file once
print(myfile)

print(myfile.read()) 
myfile.seek(0)
print(myfile.read())

print(myfile.readline())
print(myfile.readline())

print(myfile.readlines())

myfile.close()

with open('Test.txt', mode='r+') as my_file: # Read and write
    text = my_file.write('The text added using .write')
    print(text)


with open('Test.txt', mode='a') as my_file: # Read and write
    text = my_file.write('\nAppended Text')
    print(text)


with open('Happy.txt', mode='w') as my_file: # Read and write
    text = my_file.write(':D :)')
    print(text)
    

#pathlib

try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File Not Found')
    raise err
    


    