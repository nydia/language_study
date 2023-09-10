# -*- coding:utf-8 -*-
'''
Created on 2016年11月22日

@author: lvhq
'''

if __name__ == '__main__':
    database = [
            ['albert','1234'],
            ['dilbert','4242'],
            ['smith','7524'],
            ['jones','7524']
    ]
    
    username = raw_input('User name : ')
    pin = raw_input('PIN code : ')
    if[username, pin] in database : print 'Access granted'
    