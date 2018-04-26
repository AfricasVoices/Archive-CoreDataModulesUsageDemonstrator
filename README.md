# Core Data Use Demonstrator
A simple example project which shows how to import and use a cleaning function from [CoreDataModules](https://github.com/AfricasVoices/CoreDataModules).

### Instructions for Running Locally
1. Install [pipenv](https://docs.pipenv.org/#install-pipenv-today). The easiest way to do this is `$ brew install pipenv` or `$ pip install pipenv`. This project was developed with pipenv version 11.10.0. 

1. Install project dependencies with: `$ pipenv sync`.

1. Run this project with `pipenv run python demo.py`.


### Steps Undertaken to Produce this Project
For reference, these instructions describe how to set-up a new project to be able to use CoreDataModules.

1. Install [pipenv](https://docs.pipenv.org/#install-pipenv-today). The easiest way to do this is `$ brew install pipenv` or `$ pip install pipenv`. This project was developed with pipenv version 11.10.0. 

1. Set-up a pipenv environment which uses Python 2: `pipenv --two`.

1. Install CoreDataModules as an application dependency: `$ pipenv install -e git+https://www.github.com/AfricasVoices/CoreDataModules@v0.1#egg=CoreDataModules`. Note that "@v0.1" informs pipenv to install the commit of CoreDataModules tagged as "v0.1". PyPI dependencies can be installed similarly to `pip install` e.g. `$ pipenv install numpy`.

1. Write an application which depends on CoreDataModules. For a trivial example, see `demo.py`.

1. Run your application with `pipenv run python <main_file.py>` e.g. `pipenv run python demo.py`.

