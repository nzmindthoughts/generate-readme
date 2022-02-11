.PHONY: test clean deploy

all:
	@echo "ERROR: noop"
	@exit 1

test:
	@python3 -m unittest discover
	@echo "OK: $@"

deploy:
	@python3 ./deploy/deploy.py --account_number $(ACCOUNT_NUMBER) --aws_environment $(ENVIRONMENT_NAME)
	@echo "OK: $@"

readme:
	@python3 ./generate_readme/readme_script.py
	@echo "OK: $@"

clean:
	@for f in `find . -name '*.pyc'`;do rm -rf $$f; done
	@echo "OK: $@"