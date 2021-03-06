# SED Web Registration Application Development

This program is in development and is to be used for the Mitre Scout Engineering Day as a Registration Web Service. The front end of the registration service and is written in HTML, JavaScript, Python and CSS; while to back end is done using MySQL. Anyone who would like to help with development please contact Ryan Dufrene at rdufrene@mitre.org.


# Installation

The following tools are needed:
- [Git Bash](https://git-for-windows.github.io/)
- [Python](https://www.python.org/downloads/) (**Hint:** Make sure to check add to PATH if downloading version 2.7+)
- [MySQL workbench](http://dev.mysql.com/downloads/workbench/)
- [MySQL_connector](https://dev.mysql.com/downloads/connector/c/6.0.html)(**Hint:** Make sure compatible with Python version)
- [MySQL_python](https://pypi.python.org/pypi/MySQL-python/1.2.5)(**Hint:** Make sure compatible with Python version)


## Contributing
1. Fork the project
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request


## First Time Setup
### Initial Setup MySQL workbench Database (**Hint:** data will be used for later step)
1. Create a local instance of MySQL connection (**Hint:**'USER', 'PASSWORD','HOST','PORT')
2. Once connection is created, a schema would have to be generated.(**Hint:**'Schema name')


### Setup Local
1. Open Git Bash
2. Install Django `pip install Django==1.10.2`
  * **Hint:** If it does not recognize pip you need to add the Python bin folder to Environment Variable PATH.
  * **Hint:** If you are within a company firewall you will have to use `pip install --proxy <proxy> Django==1.10.2`
3. Install Django Form Tools `pip install django-formtools`
4. Install Stripe `pip install --index-url https://code.stripe.com --upgrade stripe`
5. Install MySQL_connector and MySQL_python (**Hint:** Windows can just run included files/ linux run pip install)
6. Open location of source code `cd /locationofcode/sed`
7. Open location `cd SED/settings.py` and navigate to database section and fill the data above into the corresponding location.
8. Setup the Database `python manage.py makemigrations`
9. Apply Database `python manage.py migrate`
10. Return to MySQL workbench and run the current `testscript.sql` to update the database with the test dataset. Then run step 7-8 again.
11. Run the server `python manage.py runserver`
  * Do not close the Git Bash window it is running the server.
12. Go to [http://localhost:8000/](http://localhost:8000/) in browser


## Useful Django Commands
- inital commands:
* When database have been altered: `python manage.py makemigrations` 
* When database alter has occured and need update: `python manage.py migrate`
* To run the machine on localhost port 8000: `python manage.py runserver 0.0.0.0:8000`
* This will create you an admin level account: `python manage.py createsuperuser` (**Hint:** Put `winpty` before if you get an error)
- commands afterwards:
* When database have been altered: `python manage.py makemigrations sedUI`
* When database alter has occured and need update: `python manage.py migrate sedUI`* To run the machine on localhost port 8000: `python manage.py runserver 0.0.0.0:8000`

## URLs:

- Local host urls:
* [http://localhost:8000/](http://localhost:8000/): Local Website Home Page
* [http://localhost:8000/admin/](http://localhost:8000/admin/): Local	Admin Page

- Main Test Website url:
* [http://www.sedteam.com:8000/](http://www.sedteam.com:8000/): Website Home Page
* [http://www.sedteam.com:8000/admin/](http://www.sedteam.com:8000/admin/): Website Admin Page

**Note: There might be some rendering issue when first running on the Mitre network. You might have to run as admin first beforehand.

## Design

![ScoutEngineeringDayWebDesign.png](ScoutEngineeringDayWebDesign.png?raw=true "Scout Engineering Day Web Design")


## Database Design Schema:

![Relationship_Schema.png](Relationship_Schema.png?raw=true "Scout Engineering Day Database")


## To Do

- [x] Finish Navbar
- [x] Create Home page
- [x] Create Login page
- [x] Create Register page
- [x] Create Course List page
- [x] Create Scout List page
- [x] Create Single Scout page
- [x] Create Single Course page
- [x] ~~Create PHP connection to the database~~
- [x] Create getScoutInfoFromDatabase()
- [x] Create getAllScoutsFromDatabase()
- [x] Create getCourseInfoFromDatabase()
- [x] Create getAllCoursesFromDatabase()
- [x] Create models to show about and home page data for admin modification 
- [x] update the admin page to be able to view more data
- [x] Fix bugs created when switching to Django
- [x] Add MySQL database
- [x] Update Registration process
- [ ] Scout detail page button functionalities 
- [ ] Integrate the Stripe Payment process

## Credits

* **Sue Kim**: Manager - *Initial work*
* **Ryan Dufrene**: Front-End Developer - *Initial work*
* **Walter Hiranpat**: AWS, Django Back-End Developer, Database Developer - *Initial work*
* **Edward Gedeon**: Front-End Developer - *Initial work*
