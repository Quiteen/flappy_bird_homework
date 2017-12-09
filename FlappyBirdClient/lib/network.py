# -*- coding: utf-8 -*-
import socket, netstream
connected = False
sock = None

serialID = 0            #server向客户端发回的序列ID号
isSet = False

def connect(gameScene):
    global connected, sock
    if connected:
        return connected
    #connect server
    host = "127.0.0.1"
    port = 9234
    sock = socket.socket()
    try: 
    	sock.connect((host, port))
    except:
    	connected = False
    	return connected
    
    connected = True

    #始终接收服务端消息
    def receiveServer(dt):
    	global connected, serialID
        if not connected:
            return
        data = netstream.read(sock)
        if data == netstream.TIMEOUT or data == netstream.CLOSED or data == netstream.EMPTY:
            return
        
        #客户端SID
        if 'sid' in data:
            serialID = data['sid']

        if 'notice_content' in data:
            import game_controller
            game_controller.showContent(data['notice_content']) #showContent is from game_controller
        if 'response' in data:
            import game_controller
            game_controller.showContent(data['response']) #showContent is from game_controller
            if data['response'] == u"登录成功":
                import game_controller
                game_controller.login_success()


    gameScene.schedule(receiveServer)
    return connected

def get_send_data():
    send_data = {}
    send_data['sid'] = serialID
    return send_data

#向server请求公告
def request_notice():
    send_data = get_send_data()
    send_data['type'] = 'notice'
    send_data['notice'] = 'request notice'
    netstream.send(sock, send_data)

def post_score(score):
    send_data = get_send_data()
    send_data['type'] = 'score'
    send_data['score'] = score
    netstream.send(sock, send_data)

def request_login(username, password):
    recv_message = 0
    send_data = get_send_data()
    send_data['type'] = 'login'
    send_data['username'] = username
    send_data['password'] = password
    print "send login"
    print send_data['username']
    print send_data['password']
    netstream.send(sock, send_data)

def request_register(username, password):
    recv_message = 0
    send_data = get_send_data()
    send_data['type'] = 'register'
    send_data['username'] = username
    send_data['password'] = password
    print "send register"
    print send_data['username']
    print send_data['password']
    netstream.send(sock, send_data)
