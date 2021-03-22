develop_build:
	sudo docker build -t family-wallet .
	sudo docker run -e DEVELOPMENT=False --env-file='.env' -p 9000:8080 family-wallet

push_to_ecr:
	docker build -t lambda-family-wallet .
	aws ecr get-login-password | docker login --username AWS --password-stdin 930562491335.dkr.ecr.us-east-1.amazonaws.com
	aws ecr create-repository --repository-name lambda-family-wallet --image-scanning-configuration scanOnPush=true || true 
	docker tag lambda-family-wallet:latest 930562491335.dkr.ecr.us-east-1.amazonaws.com/lambda-family-wallet:latest
	docker push 930562491335.dkr.ecr.us-east-1.amazonaws.com/lambda-family-wallet:latest
