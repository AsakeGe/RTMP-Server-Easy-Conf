# -*- coding:utf-8 -*-

import socket 
import hashlib
import os
from subprocess import run

#获取主机IP
def Get_Host_IP():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return (IP)

#SHA512加密
def HASH(sou):
    SHA512=hashlib.sha512()
    SHA512.update(bytes(sou,encoding='utf-8'))
    return(SHA512.hexdigest())

#RTMP.conf写入
def CONF_WRITE (max_connection,rtmp_port,chunk_size,application_name,server_status_port):
    conf = open("./nginx/conf/RTMP.conf","w+")
    conf.write("worker_processes  1;\n\nevents {\n\tworker_connections\t")
    conf.write(max_connection)
    conf.write(";\n\t}\nrtmp {\n\tserver {\n\tlisten\t")
    conf.write(rtmp_port)
    conf.write(";\n\tchunk_size\t")
    conf.write(chunk_size)
    conf.write(";\n\tapplication\t")
    conf.write(application_name)
    conf.write("{\n\tlive on;\n\t}\n\t}\n\t}\nhttp {\n\tinclude\tmime.types;\n\tdefault_type  application/octet-stream;\n\tsendfile\ton;\n\tkeepalive_timeout\t65;\n\nserver {\n\tlisten\t")
    conf.write(server_status_port)
    conf.write(";\n\tserver_name  localhost;\n\tlocation /stat {\n\trtmp_stat all;\n\trtmp_stat_stylesheet stat.xsl;\n\t}\n\tlocation /stat.xsl { \n\troot ./rtmp-module/;\n\t}\n\tlocation / {\n\t root   html;\n\tindex  index.html index.htm;\n\t }\nerror_page   500 502 503 504  /50x.html;\nlocation = /50x.html {\nroot   html;\n}\n}\n}")
    conf.close()

#路径获取&Nginx启动参数
def CLI():
    path = os.getcwd()
    cmd = "cd "+path + "\\nginx&&.\\nginx.exe -c \conf\RTMP.conf"
    return cmd
 
def MAIN():
    ip = Get_Host_IP()
    stream_name = input('键入直播流名称：')
    port = input('设置RTMP服务器服务端口（范围：0-65535；不可用特殊端口）：')
    max_connection = input('设置最大连接数目（不知道请输入：1024）：')
    chunk = input('设置数据流分块大小（不建议过大或过小；不知道请输入：4096）：')
    server_ststus_port = input('设置服务器状态查看端口（范围：0-65535；不可用特殊端口；不知道请输入：8080）：')
    CONF_WRITE(max_connection,port,chunk,stream_name,server_ststus_port)
    key = HASH(stream_name)
    print('服务器地址：rtmp://%s:%s/%s'%(ip,port,stream_name))
    print('串流密钥：%s'%(key))
    print('直播观看地址：rtmp://%s:%s/%s/%s'%(ip,port,stream_name,key))
    print('服务器状态查看地址：http://%s:%s/stat'%(ip,server_ststus_port,))

def run_cmd( cmd_str='', echo_print=1):
    if echo_print == 1:
        print('\n执行cmd指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)

if __name__ == "__main__":
    MAIN()
    run_cmd(CLI(),1)


       


