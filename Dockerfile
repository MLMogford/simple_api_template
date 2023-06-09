FROM python:3.11

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/diabetes-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./diabetes-api /opt/diabetes-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/diabetes-api/requirements.txt

RUN chmod +x /opt/diabetes-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
