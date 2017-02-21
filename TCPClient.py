import socket
def treebody(fileuri):
##create xml tree body from local xml file
    f = open(fileuri,'r')
    treebody = f.read()
    f.close()
    return treebody

def xml(str, uri = "C:\\rev.xml"):
##use for create local xml file from string
    f=open(uri,"w+")
    f.write(str)
    f.close()
    return

def proxycmd(message,host="15.38.201.148",timeout=15): 
##proxy clinet
    port=10000
    BUFF_SIZE = 1024 # 4 KiB
    chunk = ""
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    s.send(bytes(message,encoding='utf8'))
    s.settimeout(timeout)
    while True:
        try:
            buf = s.recv(BUFF_SIZE)
        except socket.timeout as e:
           err = e.args[0]
           if err == 'timed out':
               print ('recv timed out, retry later')
               continue
           else:
               print (e)
               s.close()   
        #print('len(buf) =  %s' % (len(buf)))
        if len(buf) == 0:
            break
        chunk += buf.decode("utf-8")   
    s.close()
    return chunk
