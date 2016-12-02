FROM python:3.5
RUN pip install boto3
VOLUME /root/.aws
VOLUME /root/outcomes
COPY credentials /root/.aws/
COPY config /root/.aws/
COPY test.py /root
WORKDIR /root

CMD python test.py
