from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker_migration_tracking.migration_path import MigrationPath

class MigrationPath:
    def __init__(self,
                path_id: int,
                species: str,
                start_location: Habitat,
                destination: Habitat,
                duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration
    
    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def schedule_migration(migration_path: MigrationPath) -> None:
        pass







    


