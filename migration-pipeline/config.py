from dataclasses import dataclass
@dataclass
class Config:
    app_name: str = "MigrationPipeline"
    log_level: str = "INFO"