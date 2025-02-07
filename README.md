# Python Tavern API Testing Framework

A repository demonstrating API testing automation using Tavern with pytest.

## Overview

This framework uses [Tavern](https://tavern.readthedocs.io/en/latest/), a pytest plugin for API testing, to create maintainable and reusable test suites for RESTful APIs.

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sarvesh371/python-tavern-automation.git
cd python-tavern-automation
```

2. Install dependencies:
```bash
sh venv_setup.sh
```

## Project Structure

```
python-tavern-automation/
├── conftest.py
├── pytest.ini
├── test_sample_test.tavern.yaml
├── requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest test_sample_test.tavern.yaml
```

## Test Reports

This project uses Allure for test reporting.

View Allure reports:
```bash
allure serve
```

## Documentation References

- [Tavern Documentation](https://tavern.readthedocs.io/en/latest/)
- [pytest Documentation](https://docs.pytest.org/en/7.1.x/)
- [Allure Reports](https://docs.qameta.io/allure/)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
