file=open(&quot;pythonfile.txt&quot;,&quot;w&quot;)
file.write(&quot;1. Python was invented by Guido van Rossum.\n2. It is easy to use and Learn.\n3. It supports
Object Oriented programming &quot;)
file.close()

file=open(&quot;pythonfile.txt&quot;,&quot;r&quot;) #(&quot;filename&quot;,&quot;mode of file&quot;)(there are 6 mode)
file.seek(0,0)
ff=file.readlines()

for x in range(0,len(ff)):
print(ff[x])
print()
print(ff)
file.close()
