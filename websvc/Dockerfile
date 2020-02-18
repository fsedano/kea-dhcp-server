FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3
RUN apt-get -y install mariadb-client python3-pip
EXPOSE 8001
WORKDIR /app
COPY src/* /app/
RUN pip3 install -r requirements.txt
CMD ["/bin/bash", "-c", "sleep 99999"]
#uvicorn --reload websvc:app --port 8001 --host 0.0.0.0