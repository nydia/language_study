# -*- coding:utf-8 -*-
'''
Created on 2016年12月22日

@author: lvhq
'''

if __name__ == '__main__':
    # 使用get（）的简单数据库
    
    #这里添加代码4-1中插入数据库的代码
    people = {
        'Alice' :{
            'phone' : '2341',
            'addr' : 'Foo drive 23'
        },
        'Beth' : {
            'phone' : '9102',
            'addr' : 'Bar street 42'
        },
        'Cecil' :{
            'phone' : '3158',
                'addr' : 'Baz avence 90'
        }
    }
    
    labels = {
        'phone' : 'phone number',
        'addr' : 'address'
    }
    
    name = raw_input('Name:')
    
    #查找电话号码还是地址
    request = raw_input('Phone number (p) or address (a)? ')
    
    #使用正确的键
    key = request #如果既不是'p' 也不是'a'
    if request == 'p' : key='phone'
    if request == 'a' : key='address'
    
    #使用get()提供默认值
    person = people.get(name,{})
    label = labels.get(key,key)
    result = person.get(key,'not available')
    
    print "%s's %s is %s." % (name, label, result)