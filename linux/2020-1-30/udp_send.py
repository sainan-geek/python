from socket import *

# 1.创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 2.准备接收方地址
dest_add = ('192.168.117.1', 8080)

# 3.从键盘获取数据
send_data = input("请输入要发送的数据：")
# 4.发送数据到电脑上指定的程序中
udp_socket.sendto(send_data.encode('utf_8'),dest_add)

# 5.关闭套接字端口
udp_socket.close()