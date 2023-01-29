# start by pulling the python image
#FROM python:3.8-alpine
FROM python:3.8.7-slim
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app


#RUN apk update
#RUN apk add git
#RUN pip install git+https://github.com/JMendes1995/py_heideltime.git

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

RUN pip3 install --upgrade pip setuptools
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

#RUN chmod -R +x /usr/local/lib/python3.8/site-packages/py_heideltime/Heideltime/TreeTaggerLinux/bin/
# copy every content from the local file to the image

EXPOSE 5000
ENV FLASK_APP=server.py

COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "flask" ]

CMD ["run", "--host", "0.0.0.0"]
