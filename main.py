from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e