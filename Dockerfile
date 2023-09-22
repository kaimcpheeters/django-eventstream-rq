FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Adds our application code to the image
COPY . workspace
WORKDIR workspace

EXPOSE 8000

# We only use docker locally so no need to set PROD command 
CMD echo "need to set a command"