from redisworks import Root
from superstructure.geist import Bewusstsein

# TODO find way to pickle objects


def main():
    root = Root  # redis.Redis('localhost')
    try:
        weltgeist = root.weltgeist
    except BaseException:
        print("Creating new weltgeist")
        weltgeist = Bewusstsein(name="Weltgeist")
        root.weltgeist = weltgeist

    # print(weltgeist)
    print(root.weltgeist)
    root.weltgeist.spill()


if __name__ == "__main__":
    main()
