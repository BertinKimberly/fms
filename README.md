# Freelance Management System

This is a Django-based web application that allows freelance managers and clients to streamline project management.

### Features

- User Authentication: Secure login and registration for freelancers, clients, and admins.
- Project Management: Create, update, and delete projects with milestones and tasks.
- Task Assignment: Assign tasks to specific freelancers, with status tracking and deadlines.

#### Technologies Used
- `Backend`: Django
- `Frontend`: HTML, CSS
- `Database`: PostgreSQL

## Installation

#### Prerequisites
- Python 3.8+
- PostgreSQL 

## Setup
### Clone the repository:

```bash
git clone https://github.com/BertinKimberly/fms.git

cd fms
```

### Install dependencies:
```bash
pip install -r requirements.txt
```


### Database setup:

- Ensure your database server is running and create a database for the project.
- Update the `DATABASES` setting in `settings.py` to match your database credentials.
### Apply migrations:
```bash
python manage.py migrate
```


