import itertools

import click
from superstructure.infrastructure.logo import print_logo
from superstructure.infrastructure.storage.pickled import load, save
from superstructure.metastructure.geist import Bewusstsein


@click.command()
@click.option("--name", default="weltgeist", help="Which Bewusstsein are we loading?")
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
def cli(name, verbose):
    if verbose:
        click.echo("[verbose mode]\n")
    print_logo()
    b = load(name=name)
    if b is not None:
        print(f"{b} woke up!")
    else:
        b = Bewusstsein(name=name, verbose=verbose)
        print(f"Created {b}")
    b.spill()
    begriff_id_combos = list(itertools.product(b._begriffe.keys(), start=1, repeat=2))
    for (a_id, b_id) in begriff_id_combos:
        relations = [relation.name for relation in (b.determine_relations(a_id, b_id))]
        if len(relations) > 0:
            print(f"{b.get(a_id).name} and {b.get(b_id).name}: {relations}")
    save(b)


if __name__ == "__main__":
    cli()
