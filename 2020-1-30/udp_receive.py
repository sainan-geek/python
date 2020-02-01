from socket import *

# 1.创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 2.准备接收方地址
dest_addr = ('', 7788)

# 3.从键盘获取数据
send_data = input("请输入要发送的数据：")

# 4.发送指定数据到指定的电脑上
udp_socket.sendto(send_data.encode('gbk'), dest_addr)

# 5.等待发送方发送数据
recv_data = udp_socket.recvfrom(1024)

# 6.显示对方发送的数据
# 接收到的数据recv_data是一个元组
# 第一个元素是对方发送的数据
# 第二个元素是对方发送的ip和端口
print(recv_data[0].decode('gbk'))
print(recv_data[1])

# 7.关闭套接字
udp_socket.close()
