from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evalation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"

try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e