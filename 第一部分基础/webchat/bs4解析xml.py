
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

from bs4 import BeautifulSoup
text='''
	<error>
	<ret>0</ret>
	<message></message>
	<skey>@crypt_f48aafbb_12845bf7a61b70cb3d78a04030e9dd68</skey>
	<wxsid>5jk4bT7j6aKN5vhK</wxsid><wxuin>1093130185</wxuin>
	<pass_ticket>ndXdF9slwPGwl%2FU7CMvKuwUYQBbGKfobU1uKfsPolOKE0CmRIG7m8qX7nt1w6fOR</pass_ticket>
	<isgrayscale>1</isgrayscale>
	</error>

'''
def xml_parser(text):
    dic={}
    soup=BeautifulSoup(text,'html.parser')
    div=soup.find(name='error')
    #找到error下面的孩子
    for item in div.find_all(recursive=False): #recursive 意思是只找div下面的儿子，等于True，会递归查找
        dic[item.name]=item.text
    return dic

print(xml_parser(text))