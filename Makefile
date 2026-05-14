.PHONY: validate build clean

validate:
	python3 scripts/validate_template.py

build:
	mkdocs build --strict

clean:
	rm -rf site
