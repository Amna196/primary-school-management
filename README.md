# Primary School Management API

This project implements a minimal API for managing primary school data using Django REST Framework (DRF). The system has two user roles: Staff and Guardians.

## Key Features

*   **Homework Management:**
    *   CRUD operations for homework assignments
    *   Role-based permissions to control access
*   **User Roles:**
    *   Staff: Can manage all aspects of homework and student data
    *   Guardians: Can only view homework related to their children

## Technical Stack

*   Django REST Framework
*   SQLite
*   swagger (api documentation and execution) 
*   Pytest

## CRUD APIS Testing

### Hoppscotch Test Suite

The API endpoints can be tested using the provided Hoppscotch collection.  You can import the `Homework.json` file into Hoppscotch or postman to run the tests.

![Hoppscotch Test Suite Screenshot](https://drive.google.com/file/d/1Fv7NUeXVe6ZWOZu2dG1TxEuSnVNCqF0c/view?usp=drive_link)

You can find the Hoppscotch collection file [here](https://drive.google.com/file/d/1WJ8GBy_tceoEI80RBPD7KeTVTli6oKhT/view?usp=drive_link).

## Test Cases

*   Used pytest
*   Tests covers the core functionality and permissions.
*   **Running the Tests:**
    1.  **Activate the Virtual Environment:**
        ```bash
        venv\Scripts\Activate.ps1  # For PowerShell
        ```
    2.  **Run Pytest:**
        ```bash
        pytest
        ```
        This will run all test cases.
    3.  **Verify Test Results:**
        A successful test run will show output indicating that all tests have passed.  Below is a sample screenshot of a valid test run:
        ![Pytest Successful Run Screenshot](https://drive.google.com/file/d/1bi8ulyeFABej_IyGcz6TF50If6V2rDHL/view?usp=sharing)

## Run The Project

 **Steps to Run the Project:**
    1.  **Activate the Virtual Environment:**
        ```bash
        venv\Scripts\Activate.ps1  # For PowerShell
        ```
    2.  **Run server:**
        ```bash
        python manage.py runserver 
        ```
    3. **Run url on browser:**
        http://127.0.0.1:8000/

## CRUD APIS documentation & Execution
### Swagger UI 
    1. **Activate the Virtual Environment:**
        ```bash
        venv\Scripts\Activate.ps1  # For PowerShell
        ```
    2.  **Run server:**
        ```bash
        python manage.py runserver 
        ```
    3. **Run url on browser:**
        http://127.0.0.1:8000/api/schema/swagger-ui/     

        ![Swagger Screenshot](https://drive.google.com/file/d/1MMl3VzeXSucCsjJ_FqK8_x_NT5uBGn8K/view?usp=sharing)

        
        
        





