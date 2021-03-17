#
Original Brief given [here](https://github.com/randomlyalex-codeclan/vet_management/blob/main/Brief.md).

[Link to live initial wireframe](https://www.figma.com/proto/OxInHW89YpirF3j5rPIjyr/Vetinary-Management-Wireframe?node-id=2%3A2&viewport=143%2C301%2C0.3050602376461029&scaling=scale-down)

[Quick Pres on the project](https://docs.google.com/presentation/d/1n4k5jQitCJ4OJAZo8qXIwiLWRtqqRCSv9ugXnedL52M/edit?usp=sharing)




##  Vet Practice Management | Python, Flask, Postgres

A web application used to help a Vet Practice manage their Vets available for treatments, database of customers, and animals and their treatments on the books.

## Demo

TBC to deploy

## Built using

- [Python](https://www.python.org/)
- [Flask - for MVC](https://palletsprojects.com/p/flask/) - Frontend framework
- Jinja / HTML / CSS
- [Psycopg](https://www.psycopg.org/) to connect with [Postgres](https://www.postgresql.org/) - Opens-source SQL database to store data
  
  

## Features

- Frontend designed in plain raw HTML/ Jinja / CSS
- Message bar to feedback actions to users
- All CRUD funcationality for Animals, Vets, Treatments and more
- Separate ledger for Treatment history.
- Logic included to stop the deleting of owners or Vets if they are attached to treatments or items.
- All deletes across the system act as disabling so are recoverable. 
- Only admin have an overriding ability to fully delete instances.
- Animals and Vets can be reassigned
- Animals without Owners can be taken on the books for the case of shelter work or such.


## Screenshots

#### Animated
Main Use - highlightings CRUD, disable function, orphanned animal logic and message bar prompts. 


![Most CRUD actions](https://github.com/randomlyalex-codeclan/vet_management/blob/main/screenshots/92EVOhiZ0y.gif)

## Static
Treatments Admin Page:

![1](https://github.com/randomlyalex-codeclan/vet_management/blob/main/screenshots/Screenshot%202021-03-17%20at%2018.26.59.png)
![2](https://github.com/randomlyalex-codeclan/vet_management/blob/main/screenshots/Screenshot%202021-03-17%20at%2018.27.14.png)




#### Client:

From root, assuming you have Flask installed (see pip otherwise) use command:

```
flask run
```
Please note: this is set up as development currently, do not deploy. 



#### DB

This assumes a connection locally to Postgres on default ports with dbname of vet_practice_management

```
psql -d vet_practice_management -f ./db/vet_app_tables_drop.sql
```

But can be changed in run_sql.py on line 9.




