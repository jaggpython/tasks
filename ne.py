str="new world of india india new new "

str=str.split()

fre={}

for i in str:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1

new=sorted(fre.items(),key=lambda x:x[1],reverse=True)
new1=sorted(fre.items(),key=lambda x:x[1])

print('\n Descending order:',end="")
print(dict(new))
print('\n')
print('\n Ascending Order:',dict(new1))
print('\n')


