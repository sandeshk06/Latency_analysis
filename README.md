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

## Verify


    docker-compose ps >> check for container is running or not

    Go to Browser and type : http://127.0.0.1:5000
    

![Screenshot_2022-03-06 Home(1)](https://user-images.githubusercontent.com/16614184/156911465-02040ed7-c586-47d8-b81a-fcbfeeb2a4f3.png)


### Latency audit result

![Screenshot_2022-03-06 Home(2)](https://user-images.githubusercontent.com/16614184/156911489-0aaa104c-4d59-4056-b2fd-2b44ecbba3f1.png)

### Traceroute result
![Screenshot_2022-03-06 Home(6)](https://user-images.githubusercontent.com/16614184/156911705-06ea4378-8276-4e2e-b21e-072fd3d46b3d.png)
![Screenshot_2022-03-06 Home(5)](https://user-images.githubusercontent.com/16614184/156911575-bf31c141-e5b5-4822-afd8-3da77bc2bf06.png)

### Geo Tracing result
![Screenshot_2022-03-06 Home(3)](https://user-images.githubusercontent.com/16614184/156911593-72cbbc10-6e0b-4ebd-9dad-dff629ce7456.png)
![Screenshot_2022-03-06 Screenshot](https://user-images.githubusercontent.com/16614184/156911613-5f797312-3890-4c17-b3fc-124cc61ae409.png)













