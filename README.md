В работе использовались данные
https://www.kaggle.com/fedesoriano/stroke-prediction-dataset


Установка (Windows):  

    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install -r requirements.txt

Установка (Linux):  

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Запуск train/predict модели:

  Логистическая регрессия:

    python train_pipeline.py --config_path ./configs/config_lr.yaml
    python model_predict.py --config_path ./configs/config_lr.yaml
    
  Наивный Байес:

    python train_pipeline.py --config_path ./configs/config_nb.yaml
    python model_predict.py --config_path ./configs/config_nb.yaml    

Самооценка работы:

-2) Назовите ветку homework1 (1 балл)

-1) положите код в папку ml_project

0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (~~2 балла~~)

написал в комментах что-то не очень вразумительное (1 балл)

1) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (2 баллов)

2) Проект имеет модульную структуру(не все в одном файле =) ) (2 баллов)

3) использованы логгеры (2 балла)

4) написаны тесты на отдельные модули и на прогон всего пайплайна(~~3 баллов~~)

тесты есть, но написаны плохо(1 балл)

5) Для тестов генерируются синтетические данные, приближенные к реальным (~~3 баллов~~)

генерация есть, но тоже так себе(1 балл)

6) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3 балла)

7) Используются датаклассы для сущностей из конфига, а не голые dict (3 балла) 

9) Обучите модель, запишите в readme как это предлагается (3 балла)

10) напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3 балла)  

13) Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1 балл доп баллы) 

Итого: 23 балла
