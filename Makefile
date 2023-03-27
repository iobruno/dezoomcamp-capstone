setup: simple-setup

simple-setup:
	@docker-compose -f docker-compose.simple.yml up -d

full-setup:
	@docker-compose -f docker-compose.complex.yml up -d

stop:
	@docker-compose -f docker-compose.complex.yml down

clean: stop
	@rm -Rf volumes/
	@docker volume prune -f
