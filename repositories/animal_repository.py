from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository


# Basic CRUD here first, inc 1 to many between animal -> vets
# Basic CRUD here first

# C --------v
def save(animal):
    sql = "INSERT INTO animals (name, dob, species, owner, treatments, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.dob, animal.species,
              animal.owner, animal.treatments, animal.vet.id]
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
        animal = Animal(row['name'], row['dob'], row['species'],
                        row['owner'], vet, row['id'])
        # this might later access a treatments table if i have time, and have a treatment history.
        animal.treatments = row['treatments']
        animals.append(animal)
    return animals


def select_id(id):
    animal = None
    sql = "SELECT * FROM animals (name, dob, species, owner, treatments, vet_id ) WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select_id(result['vet_id'])
        animal = Animal(result['name'], result['dob'], result['species'],
                        result['owner'], vet, result['id'])
        # this might later access a treatments table if i have time, and have a treatment history.
        animal.add_treatment(result['treatments'])
    return animal

# U --------v


def update(animal):
    sql = "UPDATE animals SET (name, dob, species, owner, treatments, vet_id) = (%s) WHERE id = %s"
    values = [animal.name, animal.dob, animal.species,
              animal.owner, animal.treatments, animal.vet.id, animal.id]
    run_sql(sql, values)

# D --------v


def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


# --- Extra functions after this comment
