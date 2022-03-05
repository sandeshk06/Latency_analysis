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
