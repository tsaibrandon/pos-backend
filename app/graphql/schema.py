import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, name: str) -> str:
        return f"Item {name} created!"


schema = strawberry.Schema(query=Query, mutation=Mutation)
