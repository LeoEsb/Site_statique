import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Quel est ton nom', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo('Bonjour %s!' % name)

if __name__ == '__main__':
    hello()