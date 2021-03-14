FROM amazon/aws-lambda-python:3.8
WORKDIR /var/task
COPY src/ /var/task/src
COPY requirements.txt handler.py gspread_key.json* /var/task/
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip; pip install -r requirements.txt
CMD ["handler.handler"]
