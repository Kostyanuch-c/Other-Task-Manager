### Hexlet tests and linter status:

[![Maintainability](https://api.codeclimate.com/v1/badges/185962091c55339b209b/maintainability)](https://codeclimate.com/github/Kostyanuch-c/Other-Task-Manager/maintainability)

# Task manager

[Task manager](https://task-manager-zhuv.onrender.com/) – A simple web-based task management system that allows users to
create, manage and track tasks with different statuses, assign tasks to users and filter tasks based on labels, statuses
and assignees.

### To run locally you need the following commands:

You can use the `.env_example` file provided in the repository to set up the required environment variables.  
Simply rename it to `.env` and configure the values as needed

*Also you must have [poetry](https://python-poetry.org/docs/) and [postgresql](https://www.postgresql.org/download/)
installed.*

+ **Download**
  ```bash
  git clone git@github.com:Kostyanuch-c/python-project-52.git
  ```

+ **Installing dependencies**
    ```bash
    make install
     ```

+ **For running the development server**
  ```bash
  make dev 
  ```

### Other commands that may be useful to you:

+ **Create Migrations**
  ```bash
  make create_migrations
  ```

+ **Apply Migrations**
  ```bash
  make migrate
  ```

+ **Open Django Shell**
  ```bash
  make shell
  ```

+ **Run Linters**
  ```bash
  make lint
  ```

+ **Collect Static Files**
  ```bash
  make collectstatic
  ```
