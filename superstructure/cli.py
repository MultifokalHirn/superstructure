import itertools

import click

from .infrastructure.logo import print_logo
from .metastructure.geist import Bewusstsein


@click.command()
@click.option("--name", default="Weltgeist", help="Which Bewusstsein are we loading?")
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
def cli(name, verbose):

    if verbose:
        click.echo("[verbose mode]\n")
    print_logo()
    weltgeist = Bewusstsein(name=name, verbose=verbose)
    print(weltgeist)
    weltgeist.spill()
    begriff_id_combos = list(itertools.product(weltgeist._begriffe.keys(), repeat=2))
    for (a, b) in begriff_id_combos:
        print(
            f"{weltgeist.begriff(a).name} and {weltgeist.af(b).name}: {[relation.name for relation in (weltgeist.determine_relations(a, b))]}"
        )
