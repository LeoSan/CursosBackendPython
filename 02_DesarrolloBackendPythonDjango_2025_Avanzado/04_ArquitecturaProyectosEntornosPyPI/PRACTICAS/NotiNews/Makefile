install:
	@echo "Installing dependencies..."
    uv venv
	uv sync 

run:
	@echo "Running..."
	uv pip install .
	noti-news --log-level DEBUG search "tecnologias emergentes"