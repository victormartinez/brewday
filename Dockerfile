FROM python:3.6.1

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ENV REFRESHED_AT 2017-10-24

RUN mkdir /brewday
WORKDIR /brewday
ADD requirements.txt /brewday/
ADD requirements-dev.txt /brewday/
RUN pip install -r /brewday/requirements-dev.txt
ADD . /brewday

EXPOSE 8000