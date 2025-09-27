mlog-dev:
	docker compose -f docker/docker-compose.yml up --build

mlog-down:
	docker compose -f docker/docker-compose.yml down -v

mlog-test:
	docker compose -f docker/docker-compose.yml run --rm api bash -c "PYTHONPATH=/app pytest -v"