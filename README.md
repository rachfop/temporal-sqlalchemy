# Temporal with SQLAlchemy

This project demonstrates how [Temporal](https://temporal.io/) can be combined with [SQLAlchemy](https://www.sqlalchemy.org/) to manage database operations seamlessly. Specifically, we save and retrieve greetings in a SQLite database, and these database operations are performed within Temporal activities to ensure resilience and maintainability.

## Overview

1. **Database Setup**: Using SQLAlchemy, a `Greeting` model is defined. SQLite is chosen for the database in this demonstration.
2. **Activities**: Two Temporal activities handle our database operations:
   - `save_greeting`: This activity saves a greeting message inside the SQLite database.
   - `get_latest_greeting`: This activity fetches the most recent greeting message from the SQLite database.
3. **Workflow**: The `GreetingWorkflow` performs the task of saving a greeting via the `save_greeting` activity and subsequently retrieves it using the `get_latest_greeting` activity.
4. **Main Execution**: On running the main execution, a connection is established with the Temporal service, a worker is started, and the workflow is triggered twice. Initially, with the message "first greeting" and subsequently with "second greeting".

## Requirements

- Python 3.7 or higher
- Temporal service (The default connection is set to `localhost:7233`)
- SQLAlchemy

## How to Run

1. Make sure the Temporal service is up and running. For setup, you can refer to the [Temporal Server Quick Install Guide](https://docs.temporal.io/dev-guide/python/foundations).
2. Clone the repository and navigate into the project directory.
3. To install the necessary dependencies:
   ```
   poetry install
   ```
4. To execute the program, run the worker in one terminal:
   ```
   # terminal one
   poetry run python run_worker.py
   ```
   Then, initiate the workflow in another terminal:
   ```
   # terminal two
   poetry run python run_workflow.py
   ```

Expected output:

```bash
Result: Hello, first greeting!
Result: Hello, second greeting!
```

Upon execution, you'll observe the application saving greetings and subsequently retrieving them from the SQLite database via the Temporal workflow.

## Notes

- Post execution, an SQLite database file named `hello_world.db` will be generated in the execution directory. This file will host the stored greetings.
- For more substantial, production-ready applications, consider opting for a more robust database system over SQLite. Additionally, ensure the Temporal service configurations are optimized and secure.

## Contributing

Contributions are welcome! Feel free to fork this repository, make changes, and submit pull requests. Any feedback or suggestions are highly appreciated.