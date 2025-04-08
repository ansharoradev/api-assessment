# Task 2: API Automation

Task: API automation testing framework development using
https://jsonplaceholder.typicode.com/
* Task Description: The candidate should build a complete API testing framework
using Python, pytest, and the requests library to implement atleast 2 test cases
using JSONPlaceholder API (https://jsonplaceholder.typicode.com/)
* Task Requirements:
  *  Create a modular, maintainable framework with clear separation of
  concerns
  * Implement base classes/utilities for API interactions
  * Design proper test data management
  * Include logging and reporting mechanisms
  * Test coverage should include CRUD Operations and Validations.
  * Include README with setup instructions and framework explanation

### Project Structure

* pytest.ini: Contains the logging setup using built-in pytest capability
* tests/apiclient.py: Contains the APIClient class for handling API requests
* tests/basic_tests.py: Contains test cases for CRUD operations using the JSONPlaceholder API.

### Setup
1. Clone the repository:
```
git clone git@github.com:ansharoradev/api-assessment.git
cd api-assessment
```

2. Install the dependencies:
```
conda create --name apitests -y
conda activate apitests
conda install -y --file requirements.txt
```

or if you use `pip`:
```
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Running Tests
To run the tests, use the following command:
```
pytest tests/tests_posts_api.py
```

To view a detailed report of the test results, you can use the `--html=reports/pytest_report.html` option. This will generate an HTML report of the test results in the `reports` directory.
```
pytest tests/tests_posts_api.py --html=reports/pytest_report.html
```

## Logs
The framework uses the built-in pytest capability to generate logs as defined in `api/pytest.ini` config. Additional logs are created for each CRUD operation in the `api/src/apiclient.py` class.

Logging is minimally used in the tests to emphasize readability and maintainability. The logging level is set to DEBUG by default, but can be adjusted in the `pytest.ini` file.

## Data-driven tests
The framework supports data-driven testing using the `pytest.mark.parametrize` decorator. This allows for running the same test with different sets of input data, making it easy to validate various scenarios without duplicating code.

An example of a data-driven test is `test_create_post` in the following location:
```
tests/basic_tests::test_create_post
```

It utilizes the `basic_tests.json` file located in:
```
tests/data/basic_tests.json
```

## Failures

Since this is a mock API, the following tests will fail due to missing functionality. In a real-world scenario, these tests would be implemented in the API and *should* pass.

```
FAILED tests/tests_posts_api.py::test_get_nonexistent_post - AssertionError: Response should contain an error message
FAILED tests/tests_posts_api.py::test_create_post_with_missing_title - AssertionError: Request should fail due to missing title
FAILED tests/tests_posts_api.py::test_create_post_with_empty_body - AssertionError: Request should fail due to empty body
FAILED tests/tests_posts_api.py::test_create_post_with_long_title_truncation - AssertionError: Request should fail due to longer than permitted title
FAILED tests/tests_posts_api.py::test_delete_post - AssertionError: Post should be deleted and not found
FAILED tests/tests_posts_api.py::test_delete_nonexistent_post - AssertionError: Request should fail as the post does not exist
```
