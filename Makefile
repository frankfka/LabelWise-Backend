.PHONY: deploy
deploy:
	pip3 freeze > requirements.txt && \
	gcloud config set project labelwise-app && \
	gcloud app deploy appengine.yaml

.PHONY: test
test:
	pytest