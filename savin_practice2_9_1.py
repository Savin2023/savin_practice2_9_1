# Телефонный справочник
from random import randint

#---------------------------------
def convert(my_hash):
    if my_hash<10:
        return "00"+str(my_hash)
    elif my_hash<100:
        return "0"+str(my_hash)
    else:
        return str(my_hash)


#---------------------------------
def my_hash_func(tel):
    my_hash=(hash(str(tel)))%1000
    return convert(my_hash)

#---------------------------------
tel_spr={}
key=""
tmp=0
num_koll=0

for i in range(100):
    tel=randint(1000000,9999999)
    key=my_hash_func(tel)

    while key in tel_spr:
        tmp=int(key)
#        print("Есть коллизия ",key)     # для контроля
        tmp+=1
        key=convert(tmp)
#        print("Исправлена    ",key)     # для контроля
        num_koll+=1
    tmp=0
    tel_spr[key]=tel
 
print("Всего коллизий",num_koll,"\n")
print(tel_spr)
