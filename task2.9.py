def change_list(list):
    list [0][0]=4
    print ('Значение списка после изменения значения =', list) 
    print( 'Id списка после изменения значения -', id(list))
    print( '\n')
base_list=[1,2,3]
my_list = [base_list]*3
print( 'Значение списка до вызова функции =', my_list) 
print('Id списка до вызова функции =', id(my_list))
print( '\n')
change_list(my_list)
print( 'Значение списка после вызова функции =', my_list) 
print( 'Id списка после вызова функции =', id(my_list))
print ('\n' )
