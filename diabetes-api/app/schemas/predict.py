from typing import Any, List, Optional

from pydantic import BaseModel
from regression_model.processing.validation import DiabetesDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class DiabetesDataInputs(BaseModel):
    inputs: DiabetesDataInputSchema

    class Config:
        schema_extra = {
            "example": {
                "inputs": {
                    "bmi": 0.20,
                }
            }
        }


class MultipleDiabetesDataInputs(BaseModel):
    inputs: List[DiabetesDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "bmi": 0.20,
                    },
                    {
                        "bmi": 0.020,
                    },
                    {
                        "bmi": 0.50,
                    },
                ]
            }
        }
