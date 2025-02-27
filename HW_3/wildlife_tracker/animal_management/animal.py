from typing import Optional

# WORKS
class Animal:
    def __init__(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None) -> None:
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status