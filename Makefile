DOCKER := docker
DOCKER_COMPOSE := docker-compose
API_CONTAINER := server
DB_CONTAINER := mysql
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
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK}
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db-migrate create-tables
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db stamp head
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db-migrate init


.PHONY: migrate
migrate: build
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db migrate
	${DOCKER_COMPOSE} run ${API_CONTAINER} ${FLASK} db upgrade

teardown:
	${DOCKER_COMPOSE} down


wipe: teardown
	${DOCKER} system prune --all
