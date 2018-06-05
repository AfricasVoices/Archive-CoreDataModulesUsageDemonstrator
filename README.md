# Core Data Modules Usage Samples
This repository contains simple example projects which demonstrate how
[CoreDataModules](https://github.com/AfricasVoices/CoreDataModules) may be imported and used. 
Specifically, it contains two example scripts:

1. **clean_traced** takes a JSON file containing a list of `core_data_modules.TracedData` objects and applies
   a trivial gender cleaning script from `core_data_modules` to each `TracedData` object. It outputs a new JSON
   file containing the results of the automatic cleaning, and a Coda file which contains the messages which 
   could not be coded automatically.
   
1. **merge_coda_coded** takes a JSON file containing a list of `core_data_modules.TracedData` objects and codes
   a column of this data using a Coda file which has had manual codes applied. It outputs a new JSON file
   containing a list of `core_data_modules.TracedData` objects, with the new codes applied.
   
Instructions for how to run the provided samples are given below.

## Running the Samples

### Running Locally
1. Install [pipenv](https://docs.pipenv.org/#install-pipenv-today). 
The easiest way to do this is `$ brew install pipenv` or `$ pip install pipenv`. 
This project was developed with pipenv version 2018.05.18.

1. Change your working directory to that of the sample you would like to run e.g. `$ cd clean_traced/`.

1. Install project dependencies: `$ pipenv sync`.

1. Run the project with `$ pipenv run python <project> <args>`. For example:
    1. To run `clean_traced.py`, use
       `$ pipenv run python clean_traced.py <user> <gender-col> <input> <coded-output> <coda-output>`, where:
        1. `<user>` is the name of the user running this program,
        1. `<gender-col>` is the name of the TracedData column which contains the gender values to be cleaned,
        1. `<input>` is a JSON file containing a list of the TracedData objects to be cleaned,
        1. `<coded-output>` is where the output JSON file should be written to, and
        1. `<coda-output>` is where the Coda data file for responses which could not be coded automatically should be
           written to.
           
    1. To run `merge_coda_coded.py`, use
       `$ pipenv run python merge_coda_coded.py <user> <raw-col> <code-col> <input-file> <coda-input-file> <output-file>`,
       where:
        1. `<user>` is the name of the user running this program,
        1. `<raw-col>` is the name of the TracedData column which contains the values to be coded,
        1. `<code-col>` is the name of the TracedData column which contains the coded version of the values above,
        1. `<input-file>` is a JSON file containing a list of the TracedData objects to be coded using the Coda file,
        1. `<coda-input-file>` is the Coda file containing manually coded messages, and
        1. `<output-file>` is where the output JSON file should be written to.
        
Both projects are configured to use Python 3.6 by default but all code is Python 2.7 compliant as well.

### Running in Docker
1. Install Docker. This project was tested with Docker version 18.03.0-ce, build 0520e24 on macOS.

1. Building with Docker requires ssh access to a private AVF GitHub repository, CoreDataModules. 
   For instructions on how to generate a new ssh key, and how to add this key to GitHub, refer to the
   [instructions provided by GitHub](https://help.github.com/articles/connecting-to-github-with-ssh/).

1. Change your working directory to that of the sample you would like to run e.g. `$ cd clean_traced/`.

1. Run `$ sh docker-run.sh <GitHub_key> <args>`, where 
   `<GitHub_key>` is the path to your private GitHub key described in step 2, and
   `<args>` is the list of program arguments for the program being run, as described 
   in [Running Locally](#running-locally).

## Steps Undertaken to Produce this Project
These instructions describe how to set-up a new project to be able to use CoreDataModules.

1. Install [pipenv](https://docs.pipenv.org/#install-pipenv-today). 
The easiest way to do this is `$ brew install pipenv` or `$ pip install pipenv`. 
This project was developed with pipenv version 11.10.0. 

1. Set-up a pipenv environment which uses the desired version of Python: `$ pipenv --python <version>`.
For example, for Python 2.7 use `$ pipenv --python 2.7`. This requested version of Python must be installed before
running this command.

1. Install CoreDataModules as an application dependency: 
`$ pipenv install -e git+ssh://git@github.com/AfricasVoices/CoreDataModules.git@v0.1#egg=CoreDataModules`. 
Note that "@v0.1" informs pipenv to install the commit of CoreDataModules tagged as "v0.1". 
PyPI dependencies can be installed similarly to `pip install` e.g. `$ pipenv install numpy`.

1. Write an application which depends on CoreDataModules. For a trivial example, see `demo.py`.

1. Run your application with `$ pipenv run python <main_file.py>` e.g. `$ pipenv run python demo.py`.

For Docker builds, refer to `docker-run.sh` and `Dockerfile` for an example configuration.
