
# Boilerplate FastAPI 

In order to make life easier when developing a python application, this structure was created.
Built on FastAPI integrated with tortoise orm for relational database connections.
Everything has been designed to be easy to read, maintain and scale.




## Requirements


 - Python 3 
 - Pip
 - [pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)


 ## How work

 ### Clone this repository
$ git clone <https://github.com/wesley1263/fastapi-tortoise-boilerplate.git>

### Access project directory in terminal
$ cd app_name

### Install all dependencies
$ pipenv install --dev

### Enable environment
$ pipenv shell

### Rename dotenv file
$ mv dotenv_example .env

### Run migrates
$ make migrate

### Running application in develop mode
$ python run.py

### The application is runnuing in port:8000 - acesse <http://localhost:8000/health-check> 
## Running tests

For run tests, use this commands:

```bash
  pytest 
```
or
```bash
  make testing 
```

## For create new module, use this commands:
```bash
  make create_module 
```

## Reference

 - [FastAPI Documentation](https://fastapi.tiangolo.com/)
 - [testdriven.io](https://testdriven.io/courses/tdd-fastapi/)
 - [pytest](https://docs.pytest.org/en/6.2.x/contents.html)
 - [Flake8](https://flake8.pycqa.org/en/latest/)
 - [Clean Arch](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)


## License


[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)



## Author

- [@wesley1263](https://github.com/wesley1263)


## Contributions

Contributions are welcome!


