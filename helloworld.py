# -*- coding: utf-8 -*-
#!/usr/bin/env python

def main(*unused_args):
  msg = print_me('hello world!')
  print msg

def print_me(banner):
  return banner

if __name__ == '__main__':
  main()
