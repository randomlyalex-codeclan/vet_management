class Animal():

    def __init__(self, name, dob, species, owner, vet, id=0):
        self.name = name
        self.dob = dob
        self.species = species
        self.owner = owner
        self.vet = vet
        self.treatments = ""
        self.id = id

# Currently this allows and animal to start with no treatment and then add it in later.
# This is also called in the creation of Animal objects from the database
    def add_treatment(self, treatment):
        if self.treatments != "":
            treatment = ", " + treatment
        self.treatments += treatment

    def clear_treatment_history(self):
        self.treatments = ""

    def remove_last_treatment(self):
        pass
