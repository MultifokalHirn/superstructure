import itertools

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Bewusstsein

# from superstructure.metastructure.logik import Begriff
# from superstructure.metastructure.grundbegriffe import Identität


def main(name="weltgeist", verbose=True):
    if verbose:
        print("[verbose mode]\n")
    print_logo()
    b = load(name=name)
    if b is not None:
        print(f"{b} woke up!")
    else:
        b = Bewusstsein(name=name, verbose=verbose)
        print(f"Created {b}")
    b.spill()
    # begriff_id_combos = [(begriff_id,) for begriff_id in b._begriffe.keys()]
    begriff_id_combos = list(itertools.product(b._begriffe.keys(), repeat=2))
    for (a_id, b_id) in begriff_id_combos:
        relations = [relation.name for relation in (b.determine_relations(a_id, b_id))]
        if len(relations) > 0:
            if a_id == b_id:
                topic = b.get(b_id).name
            else:
                topic = f"{b.get(a_id).name} and {b.get(b_id).name}"
            print(f"{topic} : {relations}")
    save(b)


if __name__ == "__main__":
    main()
