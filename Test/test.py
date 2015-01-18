#!/usr/bin/python
#coding=utf-8
print "欢迎老梁来到python的世界！"
item_one = 1
item_two = 2
item_three =3
#注\后面不能加东西
total = item_one + \
        item_two + \
        item_three
print total
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days[1] #python数组引用
import sys; x = 'foo'; sys.stdout.write(x + '\n')
s = 'ilovepython'
print s[1:5]
count = 0
while count < 5:
   print count, " is  less than 5"
   count ++
else:
   print count, " is not less than 5"



raw_input ("\n\n Press any key to continue!")