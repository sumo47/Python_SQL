# TO-DO List Website Development Documentation

## Project Overview

This project involved the development of a TO-DO list web application using Flask and SQLAlchemy. The application allows users to create, update, delete, and view tasks, with all data being stored in an SQLite database.

## Tools and Technologies Used

- **Flask**: A micro web framework used to build the web application.
- **SQLAlchemy**: An ORM (Object-Relational Mapper) for database operations.
- **SQLite**: A lightweight database used to store the tasks.
- **HTML/CSS**: For the front-end templates.

## Development Process

### 1. Initial Setup

- **Flask Setup**: Imported the Flask module and created an instance of the Flask class.
- **Database Configuration**: Configured the Flask application to use SQLite by setting the `SQLALCHEMY_DATABASE_URI` to `sqlite:///task.db`.
- **SQLAlchemy Setup**: Created an instance of the SQLAlchemy class and linked it to the Flask application.

### 2. Database Design

- **Task Model**: Defined a `Task` model with the following fields:
  - `sno`: An integer serving as the primary key.
  - `title`: A string field for the task title, limited to 100 characters.
  - `description`: A string field for the task description, limited to 200 characters.

### 3. Routes and Views

- **Index Route (`/`)**: 
  - Handles both GET and POST requests.
  - **GET Request**: Fetches and displays all tasks from the database.
  - **POST Request**: Retrieves task details from the form, creates a new task, and stores it in the database.

- **Contact Route (`/contact`)**:
  - Serves the contact page template.

- **About Route (`/about`)**:
  - Serves the about page template.

- **Delete Task Route (`/delete`)**:
  - Deletes a task based on the `sno` (serial number) passed as a query parameter.

- **Update Task Route (`/update`)**:
  - **GET Request**: Retrieves the task to be updated and pre-fills the form with its details.
  - **POST Request**: Updates the task in the database with the new details submitted through the form.

### 4. Running the Application

- The application is set to run in debug mode, allowing for real-time updates during development.

```python
app.run(debug=True)
```

## Conclusion

The TO-DO list application is fully functional with features to add, update, delete, and view tasks. It is designed to be a simple yet effective tool for managing personal tasks.

---

Feel free to adjust the details as needed!