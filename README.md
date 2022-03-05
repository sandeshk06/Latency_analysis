# Latency audit

Used for testing different domain latency (RTT time).

Simple python flask based application used for checking latency against domain/IP.

It will gives us following result

- Ping result (packet loss,rtt)
- MTR (Multi trace route)
- Traceroute 
- Geo path tracing for given domain
- Latency RTT (lookup time, connect time, pretransfer, transfer time, total time to connect domains)

### Prerequisites:


    Python3
    git
    curl
    
### Python Packege :

    waitress
    flask_wtf
    flask
    pycurl
    
### Installation

pip3 install waitress flask_wtf flask pycurl

### How TO run :

git clone https://github.com/sandeshk06/Latency_analysis.git
cd Latency_analysis
nohup python3 dns_app.py &

### Using Docker

git clone https://github.com/sandeshk06/Latency_analysis.git
cd Latency_analysis
docker build . -t domain_latency
docker run -d --name latency_audit -p 5000:5000 domain_latency

## Using Docker-compose

git clone https://github.com/sandeshk06/Latency_analysis.git
cd Latency_analysis
docker-compose up -d

## Veryfy

Verify:

docker-compose ps >> check for container is running or not
Go to Browser and type : http://127.0.0.1:5000







