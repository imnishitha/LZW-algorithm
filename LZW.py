from math import *
def encodeLzw( input_string ):
	for char in input_string:
		if char in dictionary:	
			continue
		else:
			dictionary.append(char)
	dictionary.sort()
	next = ""
	for char in input_string:
		a = next + char
		if a in dictionary:
			next = a
		else:
			next = a[len(a)-1]
			dictionary_word = a[0:len(a)-1]	
			dictionary.append(a)
			encoded_version.append(dictionary.index(dictionary_word))
	encoded_version.append(dictionary.index(next))		
   
def decodeLzw(encoded_version):
	x = ""	
	for i in encoded_version:
		x = x + dictionary[i]
	return x
     
def eff(dictionary,encoded_version):
    p=0
    q=0
    h=0
    l=0
    pr={}
   for i in range(0,len(dictionary)):
        p=p+len(str(bin(i)))
    for i in encoded_version:
        q=q+len(str(bin(i)))
    ef=(p-q)/p*100
    for i in range(len(encoded_version)):
        encoded_version[i]=bin(encoded_version[i])
    print("Binary Format:",encoded_version)
    dup=list(set(encoded_version)) 
    for i in dup:
        pr[i]=encoded_version.count(i)/len(encoded_version)
    for i in dup:
        l=l+(pr[i]*len(str(i)))
    for i in dup:
        h=h+(pr[i]*(log(1/pr[i],2)))
    effi=h/l*100
    print("The encoded version reduces the original text length by :",ef,"%")
    print("The entropy(H(S)) =",h)
    print("The efficiency of the code =",effi,"%")
    
dictionary = []
encoded_version = []
input_string = input("Enter a string to encode: ")
encodeLzw(input_string)
decoded_version = decodeLzw(encoded_version)
print("The encoded version of the given string is: ", encoded_version)
eff(dictionary,encoded_version)
print("The Decoded version of the encoded string is: ",decoded_version)

