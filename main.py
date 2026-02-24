from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from database import SessionLocal, init_db, Branch as DBBranch

app = FastAPI(title="Bank API Server")

@app.on_event("startup")
def on_startup():
    # Triggers the CSV loading script when the server starts
    init_db()

@strawberry.type
class BankType:
    name: str

@strawberry.type
class BranchNode:
    ifsc: str
    branch: str
    bank: BankType

@strawberry.type
class BranchEdge:
    node: BranchNode

@strawberry.type
class BranchConnection:
    edges: list[BranchEdge]

@strawberry.type
class Query:
    @strawberry.field
    def branches(self) -> BranchConnection:
        db = SessionLocal()
        try:
            # Added a limit of 100 to prevent overwhelming responses during tests
            db_branches = db.query(DBBranch).limit(100).all()
            edges = []
            for b in db_branches:
                bank_type = BankType(name=b.bank.name) if b.bank else None
                node = BranchNode(ifsc=b.ifsc, branch=b.branch, bank=bank_type)
                edges.append(BranchEdge(node=node))
            return BranchConnection(edges=edges)
        finally:
            db.close()

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/gql")

@app.get("/")
def read_root():
    return {"message": "Welcome! Go to /gql for the GraphQL interface."}