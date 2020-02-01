import socket


def send_msg(udp_socket):
    """获取键盘数据将其发送给对方"""
    # 1.获取键盘数据
    msg = input("\n请输入你要发送的数据：")

    # 2.获取对方的ip地址
    dest_ip = input("\n请输入你要发送的ip")

    # 3.获取对方的端口
    dest_port = int(input("\n请输入对方的端口"))

    # 4.发送数据
    udp_socket.sendto(msg.encode('utf-8'),(dest_ip,dest_port))


def recv_msg(udp_socket):
    """接收数据并显示"""

    # 1.接收数据
    recv_msg = udp_socket.recvfrom(1024)

    # 2.解码
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("utf-8")

    # 3.显示接收到的数据
    print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    # 1.绑定本地套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息
    udp_socket.bind(("192.168.117.1", 7891))
    while True:
        # 3.选择功能
        print("="*30)
        print("1:发送消息")
        print("2:接收消息")
        print("="*30)
        op_num = input("请输入你要操作的序号")

        # 4.根据选择调用相应的函数
        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误，请重新输入.....")

if __name__ == "__main__":
    main()