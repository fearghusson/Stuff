def randpass(letter = 7, number = 1, case = 1, special = 1):
    import random
    
    letters = {1: 'a', 2: 'b', 3: 'c', 4:'d', 5:'e', 6:'f', 7:'g',8:'h', 9:'g',
           10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q',
           18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y',
           26:'z'}
    numbers = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
               9:'9'}
    specials = {1:'!', 2:'@', 3:'#', 4:'$', 5:'%', 6:'^', 7:'&', 8:'*'}
    
    #blank lists to hold info
    pass_letter = ''
    pass_number = ''
    sorted_password = ''
    blank_list = []
    unsorted_pass = ''
    pass_special = ''
    pass_upper = ''
    
    #loops that fill the blank lists
    for iaa in range(letter):
        pass_letter += str(letters[(random.randint(1, 26))])
        
    for ibb in range(number):
        pass_number += str(numbers[(random.randint(0, 9))])
    
    for igg in range(special):
        pass_special += str(specials[(random.randint(1,8))])
    
    for ijj in range(case):
        pass_upper += str(letters[(random.randint(1, 26))])
    
    #combinded from each now filled list
    unsorted_pass = pass_letter + pass_number+ pass_special + pass_upper.upper()
    
    #takes len of unsorted_pass and takes the number value for each item in 
    #the password so that it can be randomized. blank list will look like
    #[0,1,2,3,4]
    for icc in range(len(unsorted_pass)):
        blank_list.append(icc)
    #this wil shuffle blank_list to look like [3,0,1,4,2]
    random.shuffle(blank_list)
    
    #this loop moves the values from the unsorted_pass based on the shuffled
    #blank_list
    for idd in blank_list:
        sorted_password += unsorted_pass[blank_list[idd]]
        
    print(sorted_password)
    return sorted_password
