from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


# Basic CRUD here first, inc 1 to many between animal -> vets
# Basic CRUD here first

# C --------v
def save(animal):
    sql = "INSERT INTO animals (name, dob, species, owner, vet_id, deactivated) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.species,
              animal.owner.id, animal.vet.id, animal.deactivated]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

# R  -------v


def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select_id(row['vet_id'])
        owner = owner_repository.select_id(row['owner'])
        animal = Animal(row['name'], row['dob'], row['species'],
                        owner, vet, row['deactivated'], row['id'])
        animals.append(animal)
    return animals


def select_all_active(deactivated=False):
    animals = []

    sql = "SELECT * FROM animals WHERE deactivated = %s"
    values = [deactivated]
    results = run_sql(sql, values)

    for row in results:
        vet = vet_repository.select_id(row['vet_id'])
        owner = owner_repository.select_id(row['owner'])
        animal = Animal(row['name'], row['dob'], row['species'],
                        owner, vet, row['deactivated'], row['id'])
        animals.append(animal)
    return animals


def select_id(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select_id(result['vet_id'])
        owner = owner_repository.select_id(result['owner'])
        animal = Animal(result['name'], result['dob'], result['species'],
                        owner, vet, result['deactivated'], result['id'])

    return animal

# U --------v


def update(animal):
    sql = "UPDATE animals SET (name, dob, species, owner, vet_id, deactivated) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.dob, animal.species,
              animal.owner.id, animal.vet.id, animal.deactivated, animal.id]
    run_sql(sql, values)

# D --------v


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


def delete_all_deactivated(deactivated=True):
    sql = "DELETE FROM animals WHERE deactivated = %s CASCADE"
    values = [deactivated]
    run_sql(sql, values)


def delete_id(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# --- Extra functions after this comment
