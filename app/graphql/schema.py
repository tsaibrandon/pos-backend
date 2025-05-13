from typing import List

import strawberry

from app.graphql.menu.types import MenuItem


@strawberry.type
class Query:
    @strawberry.field
    def default_menu(self) -> List[MenuItem]:
        return [
            MenuItem(
                id=1, title="Burger", price=8.99, image="https://placehold.co/400x300"
            ),
            MenuItem(
                id=2, title="Pizza", price=12.99, image="https://placehold.co/400x300"
            ),
            MenuItem(
                id=3, title="Fries", price=4.99, image="https://placehold.co/400x300"
            ),
            MenuItem(
                id=4, title="Salad", price=6.99, image="https://placehold.co/400x300"
            ),
            MenuItem(
                id=5, title="Soda", price=1.99, image="https://placehold.co/400x300"
            ),
            MenuItem(
                id=6,
                title="Ice Cream",
                price=3.99,
                image="https://placehold.co/400x300",
            ),
        ]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str) -> str:
        return f"Item {name} created!"


schema = strawberry.Schema(query=Query, mutation=Mutation)
