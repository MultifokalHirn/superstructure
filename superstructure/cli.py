import click

from superstructure.infrastructure.cli.commands import main as main_command


@click.command()
@click.option("--name", default="Weltgeist", help="Which Bewusstsein are we loading?")
@click.option("--verbose", is_flag=True, help="Will print verbose messages.")
def main(name: str, verbose: bool):
    main_command(name=name, verbose=verbose)


if __name__ == "__main__":
    main()
