FROM amazon/aws-lambda-python:3.8
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
COPY requirements.txt src/ ./
RUN pip install -r requirements.txt
CMD ["handler.handler"]
