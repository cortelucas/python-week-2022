from typing import List, Optional

import typer
from rich.console import Console
from rich.table import Table

from beerlog.core import add_beer_to_database, get_beers_from_database
from beerlog.serializers import BeerIn, BeerOut

main = typer.Typer(help="Beer management app")

console = Console()


@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
) -> BeerIn:
    """Adds a new beer to the database"""
    if add_beer_to_database(name, style, flavor, image, cost):
        print("🍺 Beer added successfully")


@main.command("list")
def list_beers(style: Optional[str] = None) -> List[BeerOut]:
    """Lists all beers in the database"""
    beers = get_beers_from_database()
    table = Table(title="Beerlog :beer_mug")
    headers = ["id", "name", "style", "flavor", "rate", "date"]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%d/%m/%Y")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
