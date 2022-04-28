from typing import List

from fastapi import FastAPI

from beerlog.core import add_beer_to_database, get_beers_from_database
from beerlog.database import get_session
from beerlog.models import Beer
from beerlog.serializers import BeerIn, BeerOut

api = FastAPI(title="Beerlog API", version="0.1.0")


@api.get("/")
def home():
    try:
        return {"message": "Welcome to the Beerlog API"}
    except Exception as exception:
        return {"message": exception}
    finally:
        pass


@api.get("/beers/")
def list_beers() -> List[BeerOut]:
    try:
        beers = get_beers_from_database()
        return {"message": "Success", "beers": beers}
    except Exception as exception:
        return {"message": exception}
    finally:
        pass


@api.post("/beers/")
def add_beer(beer_in: BeerIn) -> BeerOut:
    try:
        beer = Beer(**beer_in.dict())
        with get_session() as session:
            session.add(beer)
            session.commit()
            session.refresh(beer)

        return {"message": "Success", "beer": beer}
    except Exception as exception:
        return {"message": exception}
    finally:
        pass
