# -*- coding: utf-8 -*-
print "medio de tres numeros"

a = int(raw_input("numero 1:"))
b = int(raw_input("numero 2:"))
c = int(raw_input("numero 3:"))

if a < b:
	if b < c:
		print "el medio es %d" % b 
	elif a < c:
		print "el medio es %d" % c
	else:
		print "el medio es %d" % a
elif a < c:
	print "el medio es %d" % a
elif c < b:
	print "el medio es %d" % b
else:
	print "el medio es %d" % c 
 
