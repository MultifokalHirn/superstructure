from superstructure.hyperstructure.vernunft import (
    get_negations,
    get_relations_between_known_begriffe,
)
from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load  # , save
from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.metastructure.core import Begriff


def main(name="Weltgeist", verbose=False):
    if verbose:
        print("[verbose mode]\n")
    print_logo()
    bewusstsein = load(name=name)
    if bewusstsein is None:
        bewusstsein = Selbstbewusstsein(name=name, verbose=verbose)
        print(f"Created new Selbstbewusstsein {bewusstsein}.")
    elif verbose:
        print(f"{bewusstsein} woke up!")
    alex = Begriff(name="Alex")
    bewusstsein.learn("Alex", alex)
    bewusstsein.learn("Alexander", alex)
    bewusstsein.say(get_relations_between_known_begriffe(bewusstsein))
    bewusstsein.say(get_negations(bewusstsein))
    bewusstsein.summarize()
    # print(bool(bewusstsein))
    # print(bool(Selbstbewusstsein))
    # save(bewusstsein)


if __name__ == "__main__":
    main()
