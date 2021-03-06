from src.enities import PiplineParams, read_configs
from src.data import data_load
from src.model import train_save_model

import sys
import logging
import logging.config
import click


@click.command()
@click.option("--config_path")
def main(config_path):
    cnfg = read_configs(config_path)
    logging.basicConfig(
        stream=sys.stderr,
        level=logging.DEBUG
    )
    std_formatter = logging.Formatter(**cnfg.log_config.formatter_config)
    log_handler = logging.FileHandler(cnfg.paths.log_path)
    log_handler.setFormatter(std_formatter)
    logger = logging.getLogger('logger_all')
    logger.addHandler(log_handler)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    logger.info('Загрузка данных...')
    train, test = data_load(cnfg.paths.raw_dataset_path,
                            cnfg.train_config.test_size,
                            cnfg.train_config.random_state,
                            cnfg.paths.train_dataset_path,
                            cnfg.paths.test_dataset_path)
    logger.info('Загрузка данных завершена')
    x_train, y_train = train.drop(columns=['stroke']), train['stroke']
    x_test, y_test = test.drop(columns=['stroke']), test['stroke']
    model_type = cnfg.train_config.model_type
    metrics_path = cnfg.paths.metric_path
    model_path = cnfg.paths.output_model_path
    logger.info('Выбрана модель: ' + model_type)
    logger.info('Тренировка и сохранение модели')
    train_save_model(x_train, y_train, x_test, y_test, model_type, metrics_path, model_path)
    logger.info('Модель успешно обучена')


if __name__ == '__main__':
    main()