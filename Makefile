install:
	poetry install

project:
	poetry run project

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pipx install dist/*.whl

lint:
	poetry run ruff check .

clean:
	rm -rf dist
	rm -rf .mypy_cache
	rm -rf __pycache__