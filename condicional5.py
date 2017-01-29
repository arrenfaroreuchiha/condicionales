# -*- coding: utf-8 -*-
print "mayor medio y menor"

a = int(raw_input("numero a:"))
b = int(raw_input("numero b:"))
c = int(raw_input("numero c:"))

if a < b:
	if b < c:
		print "el medio es %d" % b
		print "el menor es %d" % a
		print "el mayor es %d" % c 
	elif a < c:
		print "por aya"
		print "el medio es %d" % c
		print "el menor es %d" % a
		print "el mayor es %d" % b 
	else:
		print "el medio es %d" % a
		print "el menor es %d" % c
		print "el mayor es %d" % b
		print "maria"
elif a < c:
	print "el medio es %d" % a
	print "el menor es %d" % b
	print "el mayor es %d" % c
	print "jonsi"
elif c < b:
	print "por aca"
	print "el medio es %d" % b
	print "el menor es %d" % c
	print "el mayor es %d" % a 
else:
	print "el medio es %d" % c
	print "el menor es %d" % b
	print "el mayor es %d" % a 
