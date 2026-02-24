from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_graphql_branches_query():
    query = """
    query {
        branches {
            edges {
                node {
                    branch
                    ifsc
                    bank {
                        name
                    }
                }
            }
        }
    }
    """
    response = client.post("/gql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    
    assert "data" in data
    assert "branches" in data["data"]
    assert "edges" in data["data"]["branches"]
    assert isinstance(data["data"]["branches"]["edges"], list)