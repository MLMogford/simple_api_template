from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from regression_model.config.core import config
from regression_model.processing.data_manager import DataInputGeneration

from app.main import app

@pytest.fixture()
def dig():
    return DataInputGeneration()



@pytest.fixture()
def test_data(dig) -> pd.DataFrame:
    return dig.load_dataset(file_name=config.app_config.testing_data_file)


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}
