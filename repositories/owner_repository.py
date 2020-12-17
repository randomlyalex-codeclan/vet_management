from db.run_sql import run_sql

from models.owner import Owner
# from models.animal import Animal


# Basic CRUD here first

# C --------v

def create_no_owner():
    sql = "UPDATE owners SET (name, address, deactivated) = (%s, %s, %s) WHERE id = %s"
    values = ["No Owner", "Holding space for orphaned and new Animals", False, 1]
    run_sql(sql, values)
    return "No Owner ID1 Created"


def save(owner):
    sql = "INSERT INTO owners (name, address, deactivated) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.name, owner.address, owner.deactivated]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

# R  -------v


def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['name'], row['address'],
                      row['deactivated'], row['id'])
        owners.append(owner)
    return owners

# the function assumes looking for active, unless overridden


def select_all_active(deactivated=False):
    owners = []
    sql = "SELECT * FROM owners WHERE deactivated = %s"
    values = [deactivated]
    results = run_sql(sql, values)

    for row in results:
        owner = Owner(row['name'], row['address'],
                      row['deactivated'], row['id'])
        owners.append(owner)
    return owners


def select_id(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['address'],
                      result['deactivated'], result['id'])
    return owner

# U --------v


def update(owner):
    # remember to change this when I add more attributes and columns later
    sql = "UPDATE owners SET (name, address, deactivated) = (%s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.address, owner.deactivated, owner.id]
    run_sql(sql, values)

# D --------v


def delete_all():
    sql = "DELETE FROM owners WHERE id > 1"
    run_sql(sql)


def delete_all_deactivated(deactivated=True):
    sql = "DELETE FROM owners WHERE deactivated = %s"
    values = [deactivated]
    run_sql(sql, values)


def delete_id(id):
    sql = "DELETE FROM owners WHERE id = %s "
    values = [id]
    run_sql(sql, values)

# --- Extra functions after this comment
