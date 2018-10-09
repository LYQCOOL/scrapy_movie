# _*_ encoding:utf-8 _*_
__author__ = 'LYQ'
__date__ = '2018/10/9 20:30'
a={'a':'b','b':'c'}
if 'd' in a.keys():
    pass
else:
    a['d']='d'
print(a)