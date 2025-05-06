from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.graphql.schema import schema
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Mount GraphQL
graphql_app = GraphQLRouter(schema, graphiql=True)
app.include_router(graphql_app, prefix="/graphql")