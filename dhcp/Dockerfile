FROM ubuntu:18.04
RUN apt-get update &&  apt-get install -y build-essential git libmariadb-dev 
RUN apt-get install -y  zlib1g-dev automake libtool pkg-config build-essential ccache libboost-dev libboost-system-dev liblog4cplus-dev libssl-dev
RUN apt-get install -y bison build-essential cmake flex libavl-dev libev-dev \
                       libpcre3-dev libprotobuf-c-dev protobuf-c-compiler swig wget

WORKDIR /app
RUN wget https://github.com/CESNET/libyang/archive/v1.0-r3.tar.gz
RUN tar zxvf v1.0-r3.tar.gz
WORKDIR /app/libyang-1.0-r3/build
RUN cmake .. && make && make install
WORKDIR /app
RUN wget https://github.com/sysrepo/sysrepo/archive/v0.7.8.tar.gz && tar zxvf v0.7.8.tar.gz
WORKDIR /app/sysrepo-0.7.8/build
RUN cmake -DCMAKE_BUILD_TYPE=Debug -DGEN_LANGUAGE_BINDINGS=ON -DGEN_CPP_BINDINGS=ON \
      -DGEN_PYTHON_BINDINGS=OFF -DGEN_LUA_BINDINGS=OFF -DENABLE_TESTS=OFF ..
RUN make && make install

###
WORKDIR /app
RUN wget https://ftp.isc.org/isc/kea/1.7.4/kea-1.7.4.tar.gz
RUN tar xvfz kea-1.7.4.tar.gz
WORKDIR /app/kea-1.7.4
RUN PKG_CONFIG_PATH=/usr/local/lib64/pkgconfig && \
            PATH="/usr/lib64/ccache:$PATH" && \
            autoreconf --install 
#RUN  ./configure --with-sysrepo && \
#            make -j4 && \
#            make install
RUN apt-get install -y libmariadbclient-dev
RUN  ./configure --with-mysql && \
            make -j4 && \
            make install
RUN echo "/usr/local/lib/hooks" > /etc/ld.so.conf.d/kea.conf && ldconfig
RUN apt-get install -y mariadb-client curl vim net-tools
COPY bootstrap.sh /app
COPY config_data/ /usr/local/etc/kea
COPY example-config.json /data/
EXPOSE 8000
CMD ["/bin/bash", "-c", "sleep 99999"]
