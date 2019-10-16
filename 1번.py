def key(str1,str2):
    answer=True
    
    if(len(str1)==len(str2)): # 문자열의 길이가 같을 때
        dic={}
        dic[str1[0]]=str2[0]
        for i in range(1, len(str1)):
            if ((str1[i] in dic)==False) and ((str2[i] in dic.values())==True) or \
            ((str1[i] in dic)==True) and (dic[str1[i]] != str2[i]):
                answer=False
                break
            dic[str1[i]]=str2[i]
        print(answer)
    else: # 문자열의 길이가 다르면 False
        print(False)
        
key('EGG','FOO')
key('ABBCD','APPLE')
key('AAB','FOO')
key('ABBCDEF','APPLEEF')
key('AABB','FOOF')