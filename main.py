import itertools

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Bewusstsein

from superstructure.metastructure.logik import Begriff

# from superstructure.metastructure.grundbegriffe import Identität


def main(name="weltgeist", verbose=False):
    if verbose:
        print("[verbose mode]\n")
    print_logo()
    bewusstsein = load(name=name)
    if bewusstsein is not None:
        print(f"{bewusstsein} woke up!")
    else:
        bewusstsein = Bewusstsein(name=name, verbose=verbose)
        print(f"Created {bewusstsein}")
    alex = Begriff(name="Alex")
    bewusstsein.learn("Alex", alex)
    bewusstsein.learn("Alexander", alex)
    # bewusstsein.spill()
    alex = bewusstsein.get("Alex")
    alexander = bewusstsein.get("Alexander")
    # begriff_combos = [(begriff_id,) for begriff_id in bewusstsein._begriffe.keys()]
    begriff_combos = [(alex, alexander)]
    begriff_combos = list(
        itertools.product(
            [bewusstsein.get(name) for name in bewusstsein.vocabulary], repeat=2
        )
    )
    for (begriff_a, begriff_b) in begriff_combos:
        relations = [
            relation.name
            for relation in (
                bewusstsein.determine_relations(begriff_a.content, begriff_b.content)
            )
        ]
        if len(relations) > 0:
            if begriff_a.name == begriff_b.name:
                topic = begriff_a.name
            else:
                topic = f"{begriff_a.name} and {begriff_b.name}"
            print(f"{topic} : {relations}")
    save(bewusstsein)


if __name__ == "__main__":
    main()
