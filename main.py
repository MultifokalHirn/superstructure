import itertools

from redisworks import Root

from metastructure.layout import print_logo
from superstructure.geist import Bewusstsein


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
    for (begriff_idA, begriff_idB) in begriff_id_combos:
        print(
            f"{weltgeist.begriff(begriff_idA).name} and {weltgeist.begriff(begriff_idB).name}: {[relation.name for relation in (weltgeist.determine_relations(begriff_idA, begriff_idB))]}"
        )
    root.weltgeist = weltgeist


if __name__ == "__main__":
    main()
