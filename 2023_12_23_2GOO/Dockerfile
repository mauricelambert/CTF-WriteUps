# start by pulling the python image
FROM debian:11

RUN apt-get update && apt-get install -y \
	python3.9 \
	python3-pip \
	python3.9-venv

RUN python3 -m venv /venv
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN /venv/bin/pip install -r requirements.txt

#RUN rm -rf /etc/machine-id
#RUN dbus-uuidgen --ensure=/etc/machine-id
# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "/venv/bin/python" ]

CMD ["run.py"]
