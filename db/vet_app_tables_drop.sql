DROP TABLE IF EXISTS vets, animals CASCADE;

CREATE TABLE vets (
    id serial PRIMARY KEY,
    name varchar(255)
);

CREATE TABLE animals (
    id serial PRIMARY KEY,
    name varchar(255),
    dob varchar(255),
    species varchar(255),
    owner VARCHAR(255),
    treatments text,
    vet_id int REFERENCES vets (id)
);

