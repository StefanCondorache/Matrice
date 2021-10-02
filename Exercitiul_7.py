coduri={\
    'a':{'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001'},
    'b':{'0':'0000','1':'0001','2':'0011','3':'0010','4':'0110','5':'0111','6':'0101','7':'0100','8':'1100','9':'1101'},
    'c':{'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'1011','6':'1100','7':'1101','8':'1110','9':'1111'},
    'd':{'0':'0011','1':'0100','2':'0101','3':'0110','4':'0111','5':'1000','6':'1001','7':'1010','8':'1011','9':'1100'}
}
print('a)Direct  b)Gray  c)Aiken  d)Exces 3')
print('Scrieti litera corespunzatoare codului:')
cod=str(input())
if cod in ['a','b','c','d']:
    print('Cate cifre doriti sa codificati:')
    nr=int(input())
    list1,list2=[],[]
    for i in range(nr):
        nri=int(input('cifra:'))
        list1.append(nri)
        list2.append(coduri[cod][str(nri)])
    print(' ',list1,'\n ',list2)
else: print('Error')