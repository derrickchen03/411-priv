from typing import Any

from wildlife_tracker_migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:
    def __init__(self,
                migration_id: int,
                start_date: str,
                current_date: str,
                migration_path: MigrationPath,
                start_location: Habitat,
                current_location: str,
                destination: Habitat,
                status: str = "Scheduled"
                ) -> None:
        self.migration_id = migration_id
        self.start_date = start_date
        self.current_date = current_date
        self.mirgration_path = migration_path
        self.start_location = start_location
        self.current_location = current_location
        self.destination = destination
        self.status = status






    