from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal
from models.treatment import Treatment

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


# Basic CRUD here first, inc 1 to many between animal -> vets
# Basic CRUD here first

# C --------v
def save(treatment):
    sql = "INSERT INTO treatments (animal_id, vet_id, date, notes, weight) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [treatment.animal_id, treatment.vet_id, treatment.date,
              treatment.notes, treatment.weight]
    results = run_sql(sql, values)
    id = results[0]['id']
    treatment.id = id
    return treatment

# R  -------v


def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    results = run_sql(sql)

    for row in results:
        treatment = Treatment(row['animal_id'], row['vet_id'],
                              row['date'], row['notes'], row['weight'], row['id'])
        treatments.append(treatment)
    return treatments


def select_all_by_animal_id(id):
    treatments = []
    sql = "SELECT * FROM treatments WHERE animal_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        treatment = Treatment(row['animal_id'], row['vet_id'],
                              row['date'], row['notes'], row['weight'], row['id'])
        treatments.append(treatment)
    return treatments


def select_all_by_vet_id(id):
    treatments = []
    sql = "SELECT * FROM treatments WHERE vet_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        treatment = Treatment(row['animal_id'], row['vet_id'],
                              row['date'], row['notes'], row['weight'], row['id'])
        treatments.append(treatment)
    return treatments


def select_id(id):
    animal = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        treatment = Treatment(result['animal_id'], result['vet_id'],
                              result['date'], result['notes'], result['weight'], result['id'])

    return treatment

# U --------v


def update(treatment):
    sql = "UPDATE treatments SET (animal_id, vet_id, date, notes, weight) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [treatment.animal_id, treatment.vet_id, treatment.date,
              treatment.notes, treatment.weight, treatment.id]
    run_sql(sql, values)

# D --------v


def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)


def delete_all_deactivated(deactivated=True):
    sql = "DELETE FROM treatments WHERE deactivated = %s CASCADE"
    values = [deactivated]
    run_sql(sql, values)


def delete_id(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# --- Extra functions after this comment
