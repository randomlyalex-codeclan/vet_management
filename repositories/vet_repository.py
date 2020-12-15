from db.run_sql import run_sql

from models.vet import Vet
# from models.animal import Animal


# Basic CRUD here first

# C --------v
def save(vet):
    sql = "INSERT INTO vets (name, deactivated) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.deactivated]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

# R  -------v


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['deactivated'], row['id'])
        vets.append(vet)
    return vets

# the function assumes looking for active, unless overridden


def select_all_active(deactivated=False):
    vets = []
    sql = "SELECT * FROM vets WHERE deactivated = %s"
    values = [deactivated]
    results = run_sql(sql, values)

    for row in results:
        vet = Vet(row['name'], row['deactivated'], row['id'])
        vets.append(vet)
    return vets


def select_id(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['deactivated'], result['id'])
    return vet

# U --------v


def update(vet):
    # remember to change this when I add more attributes and columns later
    sql = "UPDATE vets SET (name, deactivated) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.deactivated, vet.id]
    run_sql(sql, values)

# D --------v


def delete_all():
    sql = "DELETE FROM vets CASCADE"
    run_sql(sql)


def delete_all_deactivated():
    sql = "DELETE FROM vets WHERE deactivated = True CASCADE"
    run_sql(sql)


def delete_id(id):
    sql = "DELETE FROM vets WHERE id = %s "
    values = [id]
    run_sql(sql, values)

# --- Extra functions after this comment
