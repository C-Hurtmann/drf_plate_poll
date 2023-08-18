# inforce project

 Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Git
- Docker
- Docker Compose

### Installing

1. Clone the repository:
~~~
git clone https://github.com/C-Hurtmann/inforce_task
~~~
2. Build and run the Docker containers using Docker Compose:
~~~
docker-compose up --build -d
~~~
3. Go to project root dircetory:
~~~
cd inforce
~~~
4. Make migrations to database:
~~~
python3 manage.py migrate
~~~
5. Open your web browser and navigate to http://localhost:8000/ to access the API.

## Usage

Go to http://localhost:8000/swagger/ of http://localhost:8000/redoc/ to see all functions.
