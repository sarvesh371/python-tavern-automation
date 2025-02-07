import pytest
import json
import allure
from dotenv import load_dotenv

# Load .env file before tests run
load_dotenv()


@pytest.hookimpl(tryfirst=True)
def pytest_tavern_beta_after_every_response(response):
    """Hook to log a cURL command for each request in Tavern tests"""

    request = response.request
    method = request.method
    url = request.url
    headers = request.headers
    body = request.body.decode() if request.body else None

    curl_command = f"curl -X {method} '{url}'"

    if headers:
        for key, value in headers.items():
            curl_command += f" -H '{key}: {value}'"

    if body:
        curl_command += f" --data '{json.dumps(json.loads(body))}'"

    allure.attach(curl_command, name="cURL Command", attachment_type=allure.attachment_type.TEXT)
