import re
import pandas as pd
import matplotlib.pyplot as plt

def GetInfo(final_list):
    referencelist=[]
    authorlist,yearlist,titlelist,journallist=[],[],[],[]
    doilist=[]
    for f in final_list:
        # 全文
        referencelist.append(f)
        # print(f)
        # 作者
        try:
            author=re.findall(r'([A-Za-z]+ ?[A-Za-z]* ?[A-Za-z]*-?[A-Za-z]*, [A-Z]\..*?\()',f)[0].replace('(','')
        except:
            author='Null'
        authorlist.append(author)
        # print(len(author),author)

        # 年份
        try:
            year=re.findall(r'(\([0-9|a-z| ]+\))',f)[0].replace('(','').replace(')','')
        except:
            year='Null'
        yearlist.append(year)
        # print(len(year),year)

        # 标题
        try:
            title=f.split('). ')[1].replace('?','.').split('.')[0]
        except:
            title='Null'
        titlelist.append(title)
        # print(len(title),title)

        # 期刊
        try:
            # journal=f.split('). ')[1].split('.')[1].split(',')[0]
            journal=''.join(re.findall(r'.*?\)\. .*?[\.|?] (.*[,|.]?)',f)).split(',')[0]
        except:
            journal='Null'
        journallist.append(journal)
        # print(len(journal),journal)

        # DOI
        try:
            if 'doi.org' in f :
                DOI=f.split('org/')[1]
            elif 'doi:' in f:
                DOI=f.split('doi:')[1]
            else:
                DOI='Null'
        except:
            DOI='Null'
        doilist.append(DOI)
        # print('DOI:',DOI)

        # 转为数据框
        refdata={
        'Author':authorlist,
        'Year':yearlist,
        'Title':titlelist,
        'Journal':journallist,
        'DOI':doilist,
        'Reference':referencelist
        }
        refdata=pd.DataFrame(refdata)
    print(refdata)
    return refdata
# 使用内置的open函数以读取模式('r')打开文件  
yearlist = []
res = []
with open('reference.txt', 'r') as file:  
    # 读取文件内容  
    contents = file.read()
contList = contents.split("\n\n")
for ref in contList:
    try:
        matches = re.findall(r'\d{4}', ref)
    except:
        matches = None
    yearlist.append(matches[0])
for y, ref in zip(contList, yearlist):
    res.append([y, ref])
sorted_list = sorted(res, key=lambda x: x[1])
print(sorted_list)


# res = GetInfo(contList)
# print(contents)