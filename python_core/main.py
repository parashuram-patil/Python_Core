import click


@click.command()
@click.option('--name', '-n', default='there', prompt='Please ent Name', help='Name of the person to greet')
def hello(name):
    click.echo('Hello {}!'.format(name))    # used instead of print since print syntax differ by version, just a
    # safer side they say


if __name__ == '__main__':
    hello()
