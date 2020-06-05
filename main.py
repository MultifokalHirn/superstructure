from redisworks import Root
from superstructure.core import Whole, Structure, Negative


def main():
    root = Root()
    try:
        whole = root.whole
        print("Loading Whole from redis")
    except:
        print("Creating new Whole")
        whole = Whole(name="all")
        root.whole = whole
    whole.create("Being")
    being = Structure("Peter")
    whole.add(being)
    print(whole)
    # root.a = "a"


if __name__ == "__main__":
    main()
