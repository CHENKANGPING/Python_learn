import redis

r = redis.Redis(host='127.0.0.1')

pub = r.pubsub()

pub.subscribe('room_101')
pub.parse_response()

while 1:
    print("waiting for message")
    res_msg = pub.parse_response()
    print("mgs",res_msg)