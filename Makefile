mlog-dev:
	docker-compose -f docker/docker-compose.yml up --build

mlog-down:
	docker-compose -f docker/docker-compose.yml down -v

mlog-test:
	pytest -v