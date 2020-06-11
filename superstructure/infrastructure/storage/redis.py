from redisworks import Root

# this does not work!


def load(name="weltgeist"):
    root = Root  # redis.Redis('localhost')
    weltgeist = root.weltgeist  # TODO
    return weltgeist


def save(data):
    root = Root  # redis.Redis('localhost')
    root.weltgeist = data
