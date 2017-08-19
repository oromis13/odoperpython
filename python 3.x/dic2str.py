def D2str(dct):
    str=""
    for i in dct:
        str+=i+"="+dct[i]+";"
    return str

d={'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print(D2str(d))
      

    
