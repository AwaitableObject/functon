CODE = functon tests
VENV ?= .venv

TEST = pytest --verbosity=2 --showlocals --log-level=DEBUG

help: ## Show help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

test: ## Run tests
	$(TEST)

lint: ## Lint code
	pylint $(CODE)
	mypy $(CODE)

format: ## Format all files
	isort $(CODE)
	black $(CODE)