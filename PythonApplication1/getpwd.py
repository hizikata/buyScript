import msvcrt,sys

def getpwd(prompt='password:'):
    count=0
    chars=[]
    for x in prompt:
        msvcrt.putch(bytes(x,'utf8'))
    while True:
        new_char=msvcrt.getch()
        if new_char in b'\r\n':
            break
        elif new_char==b'\0x3':
            raise KeyboardInterrupt
        elif new_char==b'\b':
            if chars and count>=0:
                count-=1
                chars=chars[:-1]
                msvcrt.putch(b'\b')
                msvcrt.putch(b'\x20')
                msvcrt.putch(b'\b')
        else:
            if count<0:
                count=0
            count+=1
            chars.append(new_char.decode('utf8'))
            msvcrt.putch(b'*')
    return ''.join(chars)