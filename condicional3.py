# -*- coding: utf-8 -*-
print "menor de 3 numeros"

a = int(raw_input("numero 1:"))
b = int(raw_input("numero 2:"))
c = int(raw_input("numero 3:"))

if a < b and a < c:
  print "el menor es: %s" % a

if b < a and b < c:
  print "el menor es: %s" % b

if c < b and c < a: 
  print "el menor es: %s" % c 


         