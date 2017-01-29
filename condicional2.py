# -*- coding: utf-8 -*-
print "menor de dos numeros"

a = int(raw_input("numero 1:"))
b = int(raw_input("numero 1:"))

if a == b:
	print "son iguales"
elif a < b:
	print "el menor es: %s" % a

else:
	print "el menor es: %s" % b
