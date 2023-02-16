file1=open(&quot;pythonfile.txt&quot;,&quot;r&quot;)
for x in file1:
print(x)
file1.seek(0,0)
print(&quot; &quot;)
print()

print(&quot;Odd Line: &quot;,end=&quot; &quot;)
file2=open(&quot;odd.txt&quot;,&quot;w&quot;)
ff=file1.readlines()
with open(&#39;odd.txt&#39;,&#39;w&#39;) as file2:
for x in range(0,len(ff)):
if(x%2!=0):
print(ff[x])
file2.write(ff[x])
