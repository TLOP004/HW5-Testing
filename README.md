# Homework
- Name: Kenneth Lau 

## Question 1) Define the following unit, integration, regression tests and when you would use each?

- Unit test:  
  A unit test checks a single small piece of code in isolation (usually one function or one method).  
  It uses simple inputs and assertions to verify that the function returns the expected result or raises the expected error.  
  I use unit tests whenever I want to verify the behavior of one function/class without involving any external systems or files.

- Integration test:  
  An integration test checks how multiple units work together across module or system boundaries.  
  It often involves calling several functions together, using the real file system, or a real database/network (or realistic substitutes).  
  I use integration tests when I want to verify that end-to-end flows (e.g., loading an order, computing totals, writing a receipt) work correctly.

- Regression test:  
  A regression test is written specifically to catch a bug that was found in the past.  
  First the test fails (showing the bug), then I fix the code, and the test passes.  
  I keep the regression test in the suite so that if someone re-introduces the same bug later, the test will fail and catch it.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.

Pytest discovery:
- Pytest automatically finds tests by file and function names.
- By default, it looks for:
  - Files named `test_*.py` or `*_test.py`.
  - Inside those files, functions named `test_*`.
  - Classes named `Test*` that contain `test_*` methods.
- When I run `pytest` in the project root, it walks through subdirectories and collects all such tests.

Fixture:
- A fixture is a reusable piece of setup/teardown code that tests can depend on.
- It’s defined with `@pytest.fixture` and then injected into tests just by naming the fixture as a function parameter.
- Common uses:
  - Creating temporary data or objects.
  - Setting up database connections.
  - Using built-in fixtures like `tmp_path` to create temporary directories/files.

### Pytest features used in this homework

- `@pytest.mark.parametrize` to test multiple inputs/outputs with one test function.
- Built-in fixture `tmp_path` to create temporary files/directories in integration tests.
- `pytest.raises` to assert that functions raise the correct exceptions.

