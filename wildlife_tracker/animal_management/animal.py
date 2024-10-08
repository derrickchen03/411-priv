from typing import Any, Optional

class Animal:
    def __init__(self,
                animal_id: int,
                species: str,
                health_status: Optional[str] = None,
                age: Optional[int] = None,
                ) -> None:
        self.animal_id = animal_id
        self.age = age
        self.health_status = health_status
        self.species = species

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(eslf, animal_id: int, **kwargs: Any) -> None:
        pass