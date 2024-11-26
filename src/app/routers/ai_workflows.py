
# routers/ai_workflows.py

from fastapi import APIRouter, Depends
from app.services.model_service import ModelService

router = APIRouter(prefix="/ai", tags=["AI workflows"])

@router.post("/train")
def train_model(training_data: dict, model_service: ModelService = Depends()):
    """
    Initiates model training workflow.
    """
    result = model_service.train_model(training_data)
    return result

@router.post("/predict")
def predict(input_data: dict, model_service: ModelService = Depends()):
    """
    Generates predictions using the AI model.
    """
    prediction = model_service.predict(input_data)
    return prediction
