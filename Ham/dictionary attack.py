import hashlib

def crackHash(inputpass):
    try:
            passFile = open("wordlist.txt","r")
      
    except:
        print('could not find file') 

    for password in passFile:
               encpass=password.encode('utf-8')
               digest=hashlib.md5(encpass.strip()).hexdigest()
               if digest==inputpass:
                     print('password found:'+password)


if __name__=='__main__':
      crackHash('a9046c73e00331af68917d3804f70655')
