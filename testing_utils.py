

def verify_updated_user(response):
    """Verify that the response contains the expected updated user details."""

    response_json = response.json()


    data = response_json.get("data", {})
    assert data.get("year") == 2025
    assert data.get("price") == 1849.99
    assert data.get("CPU model") == "Intel Core i9"
    assert data.get("Hard disk size") == "1 TB"
    assert data.get("color") == "silver"

    assert "updatedAt" in response_json  # Ensure updatedAt exists in the response
