intro=input('Tell me about yourself:')
print(intro)
charcount=0
wordcount=1

for i in intro:
    charcount=charcount+1
    if(i==' '):
        wordcount=wordcount+1
print(charcount)
print (wordcount)