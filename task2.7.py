def change_string(str):
    str= 'PT1, '+str
    print( 'Значение строки после изменения значения =' , str) 
    print( 'Id строки после изменения значения =', id(str))
    print( '\n')
my_str = 'привет!'
print( 'Значение строки до вызова функции -', my_str) 
print( 'Id строки до вызова функции -', id(my_str))
print('\n')
change_string (my_str)
print ('Значение строки после вызова функции =*', my_str) 
print('Id строки после вызова функции =', id(my_str))
print ('\n')
