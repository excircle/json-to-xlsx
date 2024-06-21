# Updates docker-compose.yaml
update_password:
	@echo "Generating random password..."
	$(eval PASSWD=$(shell openssl rand -base64 12 | tr -dc 'a-zA-Z0-9' | head -c 16))
	@echo "Updating docker-compose.yaml with the generated password..."
	sed -i '' "s|REPLACEME|$(PASSWD)|g" docker-compose.yaml

# Compose up
docker_up:
	@echo "Starting Docker containers..."
	docker compose up -d

run_setup:
	@echo "Copying setup.sh to the mypy container..."
	docker cp python-home/setup.sh mypy:/tmp/setup.sh
	@echo "Making setup.sh executable..."
	docker exec mypy chmod +x /tmp/setup.sh
	@echo "Executing setup.sh inside the mypy container..."
	docker exec mypy /bin/bash /tmp/setup.sh

# make all
all: update_password docker_up run_setup

.PHONY: update_password docker_up run_setup all
