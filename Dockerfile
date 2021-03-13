FROM amazon/aws-lambda-python:3.8
WORKDIR /var/task
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
COPY src/ /var/task/src
COPY requirements.txt handler.py /var/task/
RUN pip install -r requirements.txt
CMD ["handler.handler"]
