develop_build:
	sudo docker build -t family-wallet .
	sudo docker run -e DEVELOPMENT=False --env-file='.env' -p 9000:8080 family-wallet
