import strawberry


@strawberry.type
class MenuItem:
    id: int
    title: str
    price: float
    image: str
