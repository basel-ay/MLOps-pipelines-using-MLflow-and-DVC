from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngesionConfig is a dataclass that holds the configuration for the data ingestion pipeline.
    """

    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
