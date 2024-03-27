import sys
sys.path.append("/MLOps-pipelines-using-MLflow-and-DVC/")

import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.MLOpsPipelines.entity.config_entity import PrepareBaseModelConfig