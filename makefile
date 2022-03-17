COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

formatter:
	@black .
	@isort --recursive .
	@flake8

testing:
	@pytest

create_module:
	@read -p "Enter Module Name: " MODULE \
	&& mkdir ./app/modules/$${MODULE} \
	&& mkdir ./tests/$${MODULE} \
	&& echo '' > ./app/modules/$${MODULE}/__init__.py \
	&& echo '' > ./app/modules/$${MODULE}/router.py \
	&& echo '' > ./app/modules/$${MODULE}/model.py \
	&& echo '' > ./app/modules/$${MODULE}/crud.py \
	&& echo '' > ./app/modules/$${MODULE}/schema.py \
	&& echo '' > ./app/modules/$${MODULE}/service.py \
	&& echo '' > ./tests/$${MODULE}/__init__.py \
	&& echo '' > ./tests/$${MODULE}/conftest.py \
	&& echo '' > ./tests/$${MODULE}/test_model.py \
	&& echo '' > ./tests/$${MODULE}/test_router.py \
	&& echo '' > ./tests/$${MODULE}/test_schema.py \
	&& echo "$(COLOUR_GREEN)#### MODULE $(MODULE) HAS BEEN CREATED ####$(COLOUR_END)" \
	&& echo "$(COLOUR_RED)#### DONT'T FORGET THAT ADD THIS MODULES IN app/config/settings.py ####$(COLOUR_END)"

create_topic_kafka:
	@read -p "Set the name topic: " TOPIC \
	&& docker-compose exec kafka kafka-topics --create --topic $${TOPIC} --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3

kafka_producer_console:
	@read -p "Set the name topic: " TOPIC \
	&& docker-compose exec kafka kafka-console-producer --topic $${TOPIC} --bootstrap-server kafka:9092

read_message_kafka:
	@read -p "Set the name topic: " TOPIC \
	&& docker-compose exec kafka kafka-console-consumer --bootstrap-server kafka:9092 --topic $${TOPIC} --from-beginning

run:
	@docker-compose up -d

stop:
	@docker-compose down


makemigrations:
	@read -p "set your name migration: " MIGRATION \
	&& aerich migrate --name $${MIGRATION}

migrate:
	@aerich upgrade