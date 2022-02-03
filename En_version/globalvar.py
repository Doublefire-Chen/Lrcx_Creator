#!/usr/bin/python 
# -*- coding: utf-8 -*- 
#The mode for global var reference：https://www.jb51.net/article/130193.htm#
global _global_dict
_global_dict={}
def set_value(name, value):
 _global_dict[name]=value
def get_value(name, defValue=None):
 try:
  return _global_dict[name]
 except KeyError:
  return defValue