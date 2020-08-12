import sys
buf=[]
dict1=[]
values = []
ops=[]

for line in sys.stdin:
    op, dummy, val = line.strip().split(",")
    ops.append(op.strip())
    if val.find('ffffff') != -1:
        val = (256 - int(val.replace('ffffff', ''), 16)) * -1
    else:
        val = int(val, 16)
    print hex(val)
    values.append(val)

print values
print ops
print len(values)
print len(ops)
for i in range(1,len(ops),2):
    if ops[i]=="add":
        buf.append(bytes(values[i-1]-values[i]))
    if ops[i]=="sub":
        buf.append(bytes(values[i-1]+values[i]))
    if ops[i]=="xor":
        buf.append(bytes(values[i-1]^values[i]))
print buf



