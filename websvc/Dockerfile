FROM ubuntu:18.04
RUN apt-get update && apt-get install -y python3
RUN apt-get -y install mariadb-client python3-pip libmariadbclient-dev
EXPOSE 8002
WORKDIR /app
COPY src/* /app/
RUN pip3 install -r requirements.txt
#CMD ["/bin/bash", "-c", "sleep 99999"]
CMD ["uvicorn","--reload","websvc:app","--port", "8002","--host","0.0.0.0"]