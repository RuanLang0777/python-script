import socket
import subprocess
import sys
from datetime import datetime

commonly_dict = {
    21: 'FTP',
    22: 'SSH',
    23: 'SMTP',
    53: 'DNS（UDP）',
    69: 'TFTP（cisco，类似FTP）',
    79: 'Finger',
    80: 'HTTP',
    110: 'POP3',
    111: 'RPC 远程过程调用',
    113: 'windows 验证服务',
    119: 'NNTP 网络新闻组传输协议',
    135: 'RPC 远程过程调用',
    137: 'NetBIOS',
    139: 'windows文件和打印机共享，Unix中的samba服务',
    161: 'SNMP 简单网络管理协议',
    389: 'LDAP',
    443: 'HTTPS',
    445: 'SMB',
    1080: 'socks代理服务',
    2601: 'zebra路由',
    2604: '默认密码zebra',
    5900: 'vnc',
    8080: '用户www代理服务',
}

#清除屏幕
subprocess.call('cls', shell=True)

#用户输入主机
remoteServer   = input("输入要扫描的主机(默认本机IP):")
if remoteServer == '':
    remoteServerIP ='127.0.0.1'
else:
    remoteServerIP  = socket.gethostbyname(remoteServer)

#打印主机IP
print ("-" * 60)
print ("请稍后 正在扫描主机常用端口:", remoteServerIP)
print ("-" * 60)

#获取当前时间
t1 = datetime.now()

#引入异常处理
#使用常用端口扫描范围
#初始化socket类
#建立连接
try:
    for commonly in commonly_dict:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, commonly))
        if result == 0:
            print ("[*]{}         Open         {}".format(commonly,commonly_dict[commonly]))
        sock.close()

#按键Ctrl+C退出
except KeyboardInterrupt:
    print ("手动退出")
    sys.exit()

#错误的主机名
except socket.gaierror:
    print ('无法解析主机名')
    sys.exit()

#无法连接到主机
except socket.error:
    print ("无法于主机建立连接")
    sys.exit()

#获取当前时间
t2 = datetime.now()

#计算脚本所用时间
total =  t2 - t1

#打印时间
print ('扫描所用时间:',total)
