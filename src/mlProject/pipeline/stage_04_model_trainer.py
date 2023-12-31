from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger

STAGE_NAME = "Data Validation stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
         

if __name__ == "__main__":
    try:
        logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e