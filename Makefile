# Makefile

# Activate the virtual environment and run the development server
run:
	. .venv/bin/activate && python3 manage.py runserver

# Apply migrations
migrate:
	. .venv/bin/activate && python3 manage.py migrate

# Create migrations
makemigrations:
	. .venv/bin/activate && python3 manage.py makemigrations

# Run test
test:
	. .venv/bin/activate && python3 manage.py test

# Intsall dependencies from requirements.txt
install:
	source ./venv/bin/activate && pip install -r requirements.txt

# Clean unnecessary files
clean:
	find . -name "*.pyc" -delete && find . -name "__pycache__" -delete

deactivate:


# Show help for available commands
help:
	@echo "Available commands:"
	@echo "  run            Activate the virtual environment and run the development server"
	@echo "  migrate        Apply database migrations"
	@echo "  makemigrations Create new database migrations"
	@echo "  test           Run Django tests"
	@echo "  install        Install dependencies from requirements.txt"
	@echo "  clean          Remove unnecessary files"