DROP TABLE IF EXISTS vets, owners, animals, treatments CASCADE;

CREATE TABLE vets (
    id serial PRIMARY KEY,
    name varchar(255),
    deactivated bool
);

CREATE TABLE owners (
    id serial PRIMARY KEY,
    name varchar(255),
    address varchar(255),
    deactivated bool
);

CREATE TABLE animals (
    id serial PRIMARY KEY,
    name varchar(255),
    dob varchar(255),
    species varchar(255),
    owner INT REFERENCES owners (id) ON DELETE CASCADE,
    vet_id int REFERENCES vets (id) ON DELETE CASCADE,
    deactivated bool
);

CREATE TABLE treatments (
    id serial PRIMARY KEY,
    animal_id int REFERENCES animals (id) ON DELETE CASCADE,
    vet_id int REFERENCES vets (id) ON DELETE CASCADE,
    date varchar(255),
    notes text,
    weight int
);

