install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install dist/*.whl -force-reinstall

lint:
	uv run ruff check

brain-gcd:
	uv run brain-gcd
brain-prime:
	uv run brain-prime
