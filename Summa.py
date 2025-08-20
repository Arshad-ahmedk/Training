a="Hello World"
flag=0
for ch in a.lower():
    if 'a'<=ch<='z':
        flag|=1<<(ord(ch)-ord('a'))
