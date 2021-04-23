<h1 align='center'> UniProg v1.4.7 </h1>

[![Software Engineering - Scrum Project](https://img.shields.io/badge/Software_Engineering-Scrum_Project-important)](https://github.com/rhmtazad/UniProg/) 
[![Supervisor - Mr. Ali Rahman Shinwari](https://img.shields.io/badge/Supervisor-Mr._Ali_Rahman_Shinwari-2ea44f)](https://) 
[![Made with Python](https://img.shields.io/badge/Python<=3.7-blue?logo=python&logoColor=white)](https://python.org) 
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![stars - uniprog](https://img.shields.io/github/stars/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 
[![forks - uniprog](https://img.shields.io/github/forks/rhmtazad/uniprog?style=social)](https://github.com/rhmtazad/uniprog) 

<h3 align='center'> A GUI Tool Kit for Students to Manage their Degree Plan and Courses </h3>

___  

This project was originally developed for our Software Engineering course. 
The intention of this project was to practice the software development life-cycle, 
software development practices, and different-but-related methodologies.  

The Scrum model suggests that projects progress via a series of sprints.  
In keeping with an agile methodology, sprints are timeboxed to 
no more than a month long, most commonly two weeks.

Scrum methodology advocates for a planning meeting at the start of the sprint,
where team members figure out how many items they can commit to, 
and then create a sprint backlog – a list of the tasks to perform during the sprint.  
___  


## Scrum Master and Product Owner

- Fatema Qambari (Product Owner)
- Nasrin Natiqi  (Scrum Master)

## Developer Team

- Rahmat Azad
- Mohammad Sulayman Rezaie
- Sajjad Afzali
- Tasal Sahibzadah

## User Interface Preview

### Login Portal
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/login.PNG"/>

### Sign Up Portal
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/signup.PNG"/>

### Dashboard  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/dashboard.PNG"/>  

### Degree Plan Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/degreeplan.PNG"/>  

### Courses Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/courses.PNG"/> 

### Account Portal  
<img width="800" src="https://raw.githubusercontent.com/rhmtazad/uniprog/main/screenshots/account.PNG"/>   


## Requirements

**To use this software you must have installed:**

- [Python] - Version 3.7 or other compatible versions
- [PyQt5]  - Version 5.15.2 of this framework for running the GUI
- [pandas] - Version 1.2.4 of pandas library for managing CSV files
- [numpy]  - Version 1.20.2 of numpy which comes with pandas standard library

## Installation

**To install the requirements and use the software, do the following:**

If you're using Debian Buster+:

```
$ sudo apt install pipenv
```

Or, if you're using Fedora:

```
$ sudo dnf install pipenv
```

Or, if you're using FreeBSD:

```
# pkg install py37-pipenv
```

When none of the above is an option, it is recommended to use Pipx:

```
$ pipx install pipenv
```

Then, set the current directory to the project directory

```
$ cd UniProg
```

Now, you must intall the requirements

```
$ pip install -r requirements.txt
```

To use the run the app, you can either double click on the main.py file  
or you can run the following line of code

```
$ python main.py
```


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create.  
Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/NewFeatures)
2. Commit your Changes (git commit -m 'Add some NewFeatures')
3. Push to the Branch (git push origin feature/NewFeatures)
4. Open a Pull Request

## License

GNU General Public License (GPL-3.0)  
Distributed under the GPL-3.0 License which means you can use or distribute it however you want.
