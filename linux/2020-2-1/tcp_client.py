from socket import *

# 创建socket
tcp_client_socket = socket(AF_INET, SOCK_DGRAM)

# 目的信息

sever_ip = input("请输入服务器ip 172.20.10.41 :")
sever_port = int(input("请输入服务器端口"))

# 链接服务器
tcp_client_socket.connect((sever_ip,sever_port))

# 提示用户输入数据
send_data = input("请输入要发送的数据：　")
tcp_client_socket.send(send_data.encode('utf-8'))

# 接收对方发过来的数据，最大1024字节
recvData = tcp_client_socket.recv(1024)
print("接收到的数据为：",recvData.decode('utf-8'))

# 关闭套接字　
tcp_client_socket.close()