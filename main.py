from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.metastructure.logik import Begriff
from superstructure.hyperstructure.vernunft import (
    say_all_relations_between_known_begriffe,
    say_negations,
)


def main(name="Weltgeist", verbose=False):
    if verbose:
        print("[verbose mode]\n")
    print_logo()
    bewusstsein = load(name=name)
    if bewusstsein is not None:
        print(f"{bewusstsein} woke up!")
    else:
        bewusstsein = Selbstbewusstsein(name=name, verbose=verbose)
        print(f"Created {bewusstsein}")
    bewusstsein.spill()
    alex = Begriff(name="Alex")
    bewusstsein.learn("Alex", alex)
    bewusstsein.learn("Alexander", alex)
    say_all_relations_between_known_begriffe(bewusstsein)
    say_negations(bewusstsein)
    # print(bool(bewusstsein))
    # print(bool(Selbstbewusstsein))
    save(bewusstsein)


if __name__ == "__main__":
    main()
