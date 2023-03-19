from math import isclose

import pandas as pd
from fastapi.testclient import TestClient


def test_make_stream_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    stream_data = test_data.head(1)
    payload = {"inputs": stream_data.to_dict(orient="records")}

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict_stream",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert len(prediction_data["predictions"]) == 1
    assert isclose(prediction_data["predictions"][0], 225.89193139816433, abs_tol=1e-4)


def test_make_batch_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {"inputs": test_data.to_dict(orient="records")}

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict_batch",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert len(prediction_data["predictions"]) == 20
    assert isclose(prediction_data["predictions"][0], 225.89193139816433, abs_tol=1e-4)
