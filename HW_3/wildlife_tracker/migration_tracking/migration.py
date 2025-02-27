from migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, migration_path: MigrationPath, status: str = "Scheduled"):
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.status = status