
memcached = {}
event = 'url'
feature = '192.168.0.01'
current_timestamp = 10000

def fiveQpsLimiter():
    count = 0
    for t in (0, 60):
        key = event + feature + (current_timestamp - t)
        count += memcached[key]
        if count > 5:
            return False
    return True