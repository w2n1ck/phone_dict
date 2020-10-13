#!/usr/bin/env python
a = ['11111111', '00000000','22222222','33333333','44444444','55555555','66666666','77777777','88888888','99999999','12345678']
b = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
c = ['0000','1111','2222','3333','4444','5555','6666','7777','8888','9999']
d1 = ['134','135','136','137','138','139','147','150','151','152','157','158','159','178','182','183','184','187','188']
d2 = ['130','131','132','145','155','156','185','186','176','175']
d3 = ['133','149','153','180','181','189','177']
phone = list()
for i in d1:
    for n in a:
        _ = '{}{}'.format(i, n)
        phone.append(_)
for i in d2:
    for n in a:
        _ = '{}{}'.format(i, n) 
for i in d3:
    for n in a:
        _ = '{}{}'.format(i, n) 

for i in d1:
    for n in b:
        for m in c:
            _ = '{}{}{}'.format(i, n, m)
            phone.append(_)
for i in d2:
    for n in b:
        for m in c:
            _ = '{}{}{}'.format(i, n, m)
            phone.append(_)
for i in d3:
    for n in b:
        for m in c:
            _ = '{}{}{}'.format(i, n, m)
            phone.append(_)

with open('/Users/w2n1ck/Desktop/info/phone.txt','a') as f:
    for i in phone:
        f.write(str(i) + '\n')
