#-*- coding: utf-8 -*-
#comentários de uma linha
""" comentários de varias linhas"""
print("Olá Mundo")
print("Michelle")
print(2+3)
print(2-3)
print(2*3)
print(6/2)
print(6%2)
print(2**4)
# VARIÁVEIS 
var1=1 # VARIÁVEL INTEIRO
var2=1.1 #variável tipo float
var3= "Meu nome é Michelle" #variável tipo string 
var4= True #ou False #variável boleano 

print(var1)
print(var2)
print(var3)
print(var4)

#condicionais
x=1
y=2

if (x < y and x < 0):
	print("x é negativo e menor que  y")
if (x > y and x>0):
	print("x é positivo e maior que y")
if (x < y and x > 0):
	print("x é positivo menor  que y")


x=4
y=6
if x==y:
	print("iguais")
elif y>x:
	print("y maior que x")
elif x<y:
	print("x menor que y")	
else:
	print("diferentes")	
	pass
	