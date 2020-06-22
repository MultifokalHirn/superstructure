import itertools
from typing import List

from sortedcontainers import SortedSet

from superstructure.metastructure.geist import Bewusstsein
from superstructure.metastructure.grundbegriffe import FürUnsSein, Selbstidentität
from superstructure.metastructure.core import Unknown


def get_negations(bewusstsein: Bewusstsein) -> List[str]:
    urteile = []
    no_negation = SortedSet()
    for begriff in bewusstsein.begriffe:
        if begriff.negation is None or begriff.negation == Unknown():
            no_negation.add(begriff)
        else:
            if f"{begriff.negation} and {begriff} are opposites." not in urteile:
                urteile.append(f"{begriff} and {begriff.negation} are opposites.")
    for begriff in no_negation:
        urteile.append(f"Negation of {begriff} is {begriff.negation}.")
    return urteile


def get_relations_between_known_begriffe(
    bewusstsein, accept_identicals: bool = False
) -> List[str]:
    urteile = []
    word_combos = itertools.product(
        [bewusstsein.get(name).name for name in bewusstsein.vocabulary], repeat=2
    )

    word_combos = set(frozenset(k) for k, _ in itertools.groupby(word_combos))
    # print(f"Checking Relations between the Begriffe known to {bewusstsein}")
    singular_begriffe = set()
    for combo in word_combos:
        combo = tuple(combo)
        if len(combo) == 1:
            (word_a, word_b) = (combo[0], combo[0])
        else:
            (word_a, word_b) = (combo[0], combo[1])
        if word_a == word_b:
            relations = [
                relation.name
                for relation in (
                    bewusstsein.determine_relations(
                        word_a, accept_identicals=accept_identicals,
                    )
                )
                if relation not in [FürUnsSein(), Selbstidentität()]
            ]
        else:
            relations = [
                relation.name
                for relation in (
                    bewusstsein.determine_relations(
                        word_a, word_b, accept_identicals=accept_identicals,
                    )
                )
                if relation != FürUnsSein()
            ]
        if word_a == word_b:
            topic = f"{word_a}"
            singular_begriff = bewusstsein.get(topic).begriff
            if singular_begriff in singular_begriffe:
                continue
            singular_begriffe.add(singular_begriff)
        else:
            topic = f"{word_a} and {word_b}"
        if len(relations) > 0:
            urteile.append(
                f"Relations for '{topic}': {' and '.join([str(r) for r in relations])}"
            )
    return urteile
