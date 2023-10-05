from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
         

if __name__ == "__main__":
    try:
        logger.info(f"{'>' * 7} {STAGE_NAME} started {'<' * 7}")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"{'>' * 7} {STAGE_NAME} completed {'<' * 7}\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e