DOCKER := docker
DOCKER_COMPOSE := docker-compose
API_CONTAINER := server
DB_CONTAINER := db
FLASK := flask

.PHONY: nuke
nuke:
	${DOCKER} system prune -a

.PHONY: rm-exited-containers
rm-exited-containers:
	${DOCKER} ps -a -q -f status=exited | xargs ${DOCKER} rm -v

.PHONY: up
up:
	${DOCKER_COMPOSE} up --build -d

.PHONY: setup
setup: up
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db migrate
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db upgrade


.PHONY: lint
lint:
	${DOCKER} exec ${API_CONTAINER} ${FLASK} lint

.PHONY: clean
clean:
	${DOCKER} exec ${API_CONTAINER} ${FLASK} clean

.PHONY: migrate
migrate: build
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db migrate
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db upgrade

teardown:
	${DOCKER_COMPOSE} down

wipe: teardown
	${DOCKER} system prune --all
