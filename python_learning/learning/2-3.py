# -*- coding:utf-8 -*-
'''
Created on 2016年11月22日

@author: lvhq
'''

if __name__ == '__main__':
    'Sentence : He\'s a very naught boy!'
    sentence = raw_input("Sentence:")
    screen_with = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_with - box_width) // 2
    print
    print ' ' * left_margin+ '+' + '-' * (box_width - 2) + '+'
    print ' ' * (left_margin + 2) + '|' + ' ' * text_width      + '|'
    print ' ' * (left_margin + 2) + '|' +       sentence        + '|'
    print ' ' * (left_margin + 2) + '|' + ' ' * text_width      + '|'
    print ' ' * left_margin +  '+' + '-' * (box_width -2)  + '+'
    print