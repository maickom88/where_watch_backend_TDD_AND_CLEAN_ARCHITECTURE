# type: ignore
from src.domain.entities.poster_entity import PosterEntity
from typing import List


class DetailsEntity:
    banners: List[str]
    sinopse: str
    poster_image: str
    type_poster: str
    runtime: str
    title: str
    year: str
    seansons: List[PosterEntity]
    genders: List[str]
    providers: List[str]

    def __init__(self,
                 title: str,
                 banners: List[str],
                 type_poster: str,
                 poster_image: str,
                 runtime: str,
                 year: str,
                 sinopse: str,
                 providers: List[str],
                 seansons: List[PosterEntity],
                 genders: List[str]):
        self.title = title
        self.year = year
        self.seansons = seansons
        self.genders = genders
        self.runtime = runtime
        self.banners = banners,
        self.sinopse = sinopse,
        self.type_poster = type_poster
        self.poster_image = poster_image
        self.providers = providers
        # noqa: W292
