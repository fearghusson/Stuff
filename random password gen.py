import random

letters = {1: 'a', 2: 'b', 3: 'c', 4:'d', 5:'e', 6:'f', 7:'g',8:'h', 9:'g',
           10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q',
           18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y',
           26:'z'}
numbers = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
           9:'9'}
password = ""
password_letter = ""
password_number = ""
sorted_password = ""
blank_list = []


print('just letters? yes or no')

yes_no = input()

if yes_no.lower() == 'yes':
    
   print('how long is the password?')
   all_letter_pass = int(input())
   
   for i in range(all_letter_pass):
       password += str(letters[(random.randint(1, 26))])
   print(password)
   
elif yes_no.lower() == 'no':
    print('how many letters?')
    number_of_letters = int(input())
    
    print('how many numbers?')
    number_of_numbers = int(input())
    
    for iaa in range(number_of_letters):
        password_letter += str(letters[(random.randint(1, 26))])
        
    for ibb in range(number_of_numbers):
        password_number += str(numbers[(random.randint(0, 9))])
        
    unsorted_password = password_letter + password_number
    
    for icc in range(len(unsorted_password)):
        blank_list.append(icc)
        
    random.shuffle(blank_list)
    
    for idd in blank_list:
        sorted_password += unsorted_password[blank_list[idd]]
    
    print(sorted_password)
