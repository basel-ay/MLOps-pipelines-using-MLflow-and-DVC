import os
from box.exceptions import BoxValueError
import yaml
from src.MLOpsPipelines import logger
import json
import joblib

# To make sure that our code working fine, and if not then raise exceptions.
from ensure import ensure_annotations
from box import ConfigBox
import box
from pathlib import Path
from typing import Any
import base64


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file from the given path.

    Args:
        :path_to_yaml (str): Path to the yaml file.

    Returns:
        :ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e
    

print(read_yaml(Path("params.yaml")))