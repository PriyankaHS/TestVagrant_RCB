![TestVagrant_RCB](https://user-images.githubusercontent.com/95631736/202631325-a9dd7df6-a8c1-4ac2-8e39-2cab4b08f4c1.jpg)

# TestVagrant_RCB Assesment

Root folder must be *TestVagrant_RCB*

## Technologies Used
Selenium, Python, Pytest

## Clone Framework into Your Machine
> git clone https://github.com/PriyankaHS/TestVagrant_RCB

## Navigate to Repo Folder in commend line
> cd TestVagrant_RCB

## Setup to run tests
Required -> Python(version >= 3.5.0)

## Steps to install from cmd line:
#### Pipenv 
> pip install pipenv || python3 -m pip install pipenv

## Set up venv and install packages
> pipenv install

> pip install -r requirements.txt

To execute scripts from command line
> pipenv run pytest -m marker_name

> pipenv run pytest module.py::ClassName::method_name


## To change grouping of scripts (change marker_name)
> Markers are used for grouping tests

## For reports option
> --html=report.html 

## For rerunning failed tests
> pipenv run pytest --lf

## For parallel execution 
> -n number_of_workers (input_type = integer)
