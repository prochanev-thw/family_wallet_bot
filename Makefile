rebuild:
	sudo docker build -t family-wallet .
	sudo docker run -p 9000:8080 family-wallet

develop:
	export DEVELOPMENT=True; python -m src.spreadsheets.client