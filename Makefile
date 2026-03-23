DC = docker-compose -f docker-compose.yaml
up:
	$(DC) up
down: 
	$(DC) down