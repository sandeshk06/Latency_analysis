FROM alpine:latest
LABEL maintainer="sandeshkulkarni1991@gmail.com"
RUN apk add --update python3 py3-pip python3-dev
RUN apk add --no-cache libcurl
ENV PYCURL_SSL_LIBRARY=openssl
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip3 install pycurl \
    && apk del .build-dependencies
RUN pip3 install flask waitress ipaddress pycurl
COPY check_domain_result.py   /usr/local/src/DOMAIN_LATENCY/
COPY app.py   /usr/local/src/DOMAIN_LATENCY/
COPY templates   /usr/local/src/DOMAIN_LATENCY/templates/
COPY static   /usr/local/src/DOMAIN_LATENCY/static/
WORKDIR "/usr/local/src/DOMAIN_LATENCY/"
EXPOSE 5000
ENTRYPOINT python3 app.py
