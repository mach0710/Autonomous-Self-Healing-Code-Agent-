Project Architecture

Generator Node: Creates the initial solution based on user requirements.

QA Node: Authors a test suite to verify logic and edge cases.

Executor Node: Runs the code in a Docker container and captures results.

Healer Node: Triggered on failure; reflects on the error log to refactor the code.



Dependencies

To run this project, you will need Python 3.9+ and Docker Desktop installed.
