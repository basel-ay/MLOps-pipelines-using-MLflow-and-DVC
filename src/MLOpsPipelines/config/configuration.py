import os
current_directory = os.getcwd()

import sys
sys.path.append(current_directory)

from src.MLOpsPipelines.constants import *
from src.MLOpsPipelines.utils.common import read_yaml, create_directories
from src.MLOpsPipelines.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH,
    ):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config, self.params])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
