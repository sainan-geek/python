from socket import *

# 1.创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2.绑定本地相关信息，如果不绑定，则系统会随机匹配
local_addr = ('192.168.117.1', 7788)
udp_socket.bind(local_addr)

send_addr = ('192.168.117.1', 8080)
send_data = input("请输入要发送的信息：")

udp_socket.sendto(send_data.encode('gbk'), send_addr)
# 3.等待接收对方的数据
recv_data = udp_socket.recvfrom(1024)

# 4.显示接收到的数据
print(recv_data[0].decode('gbk'))

# 5.关闭套接字
udp_socket.close()