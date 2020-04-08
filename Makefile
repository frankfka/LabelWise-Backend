.PHONY: deploy
deploy:
	pip3 freeze > requirements.txt && \
	gcloud config set project labelwise-gcp && \
	gcloud app deploy appengine.yaml