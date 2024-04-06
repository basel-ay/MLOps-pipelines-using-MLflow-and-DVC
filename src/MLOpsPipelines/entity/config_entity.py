from dataclasses import dataclass
from pathlib import Path


# Creating a dataclass with "frozen=True" means its instances are frozen and cannot be changed.


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    DataIngesionConfig is a dataclass that holds the configuration for the data ingestion pipeline.
    """

    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """
    PrepareBaseModelConfig is a dataclass that holds the configuration for our base model.
    """

    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int
