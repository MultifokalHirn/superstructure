import itertools
from sortedcontainers import SortedSet
from superstructure.metastructure.logik import Unknown
from superstructure.metastructure.grundbegriffe import FürUnsSein, Identität


def say_negations(bewusstsein) -> None:
    no_negation = SortedSet()
    for begriff in bewusstsein.begriffe:
        if begriff.negation is not Unknown():
            bewusstsein.say(f"Negation of {begriff} is {begriff.negation}")
        else:
            no_negation.add(begriff)
    for begriff in no_negation:
        bewusstsein.say(f"Negation of {begriff} is {begriff.negation}")


def say_all_relations_between_known_begriffe(bewusstsein) -> None:
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
            relations.remove(Identität().name)
            topic = f"{word_a}"
        else:
            topic = f"{word_a} and {word_b}"
        if len(relations) > 0:
            bewusstsein.say(f"{topic}: {relations}")
