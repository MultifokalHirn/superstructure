import itertools

from redisworks import Root

from superstructure.infrastructure.logo import print_logo
from superstructure.metastructure.geist import Bewusstsein


def main():
    print_logo()
    root = Root  # redis.Redis('localhost')
    try:
        weltgeist = root.weltgeist
        print(f"Loaded {weltgeist}")
    except BaseException:
        print("Creating new weltgeist")
        weltgeist = Bewusstsein(name="Weltgeist")

    weltgeist.spill()
    print(weltgeist)
    begriff_id_combos = list(itertools.product(weltgeist._begriffe.keys(), repeat=2))
    for (a, b) in begriff_id_combos:
        print(
            f"{weltgeist.begriff(a).name} and {weltgeist.af(b).name}: {[relation.name for relation in (weltgeist.determine_relations(a, b))]}"
        )
    root.weltgeist = weltgeist


if __name__ == "__main__":
    main()
