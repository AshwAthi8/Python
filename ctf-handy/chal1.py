import base64
newstr="x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q"
p=[]

ida="ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"
ori="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

for i in newstr:
	if(ida.index(i)==ori.index(i)):
		p.append(i)
	else:
		p.append(ori[ida.index(i)])

print("".join(p))
p="".join(p)
print(base64.b64decode(p))

#c2gwMHRpbmdfcGhpc2hfaW5fYV9iYXJyZWxAZmxhcmUtb24uY29t
#b'sh00ting_phish_in_a_barrel@flare-on.com'
