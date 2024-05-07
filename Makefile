.PHONY: build test

build: ## This step is empty since there is nothing really for me to build or compile yet as its just a Python script
	@echo "Building the utility..."

test:
	@echo "No test defined yet"

.PHONY: run
run:
    python3 task.py $(ARG1)
