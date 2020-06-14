import itertools

from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Selbstbewusstsein
from superstructure.metastructure.logik import Begriff
from superstructure.metastructure.grundbegriffe import FürUnsSein


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
    word_combos = itertools.product(
        [bewusstsein.get(name).name for name in bewusstsein.vocabulary], repeat=2
    )

    word_combos = set(frozenset(k) for k, _ in itertools.groupby(word_combos))
    print(f"Checking Relations between the Begriffe known to {bewusstsein}")
    for combo in word_combos:
        combo = tuple(combo)
        if len(combo) == 1:
            (word_a, word_b) = (combo[0], combo[0])
        else:
            (word_a, word_b) = (combo[0], combo[1])
        relations = [
            relation.name
            for relation in (
                bewusstsein.determine_relations(
                    bewusstsein.get(word_a).content, bewusstsein.get(word_b).content,
                )
            )
            if relation != FürUnsSein()
        ]
        if word_a == word_b:
            relations.remove("Identität")
            topic = f"{word_a}"
        else:
            topic = f"{word_a} and {word_b}"
        if len(relations) > 0:
            bewusstsein.say(f"{topic}: {relations}")
    # print(bool(bewusstsein))
    # print(bool(Selbstbewusstsein))
    save(bewusstsein)


if __name__ == "__main__":
    main()
