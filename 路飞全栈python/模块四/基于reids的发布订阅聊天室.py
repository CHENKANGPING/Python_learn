import redis
import threading

r = redis.Redis(host='127.0.0.1')

def send_msg():
    msg = input(">>>")
    r.publish("room_101",msg)

def receive_msg():
    pub = r.pubsub()

    pub.subscribe("room_101")
    pub.parse_response()

    while 1:
        res_msg = pub.parse_response()
        print(">>>",res_msg)


t = threading.Thread(target=send_msg)
t.start()

receive_msg()