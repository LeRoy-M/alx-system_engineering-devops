## 0x09. Web infrastructure design

**0. Simple web stack** `[0-simple_web_stack]` >> Whiteboard design of a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Captures:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (the code base)
- 1 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

**1. Distributed web infrastructure** `[1-distributed_web_infrastructure]` >> Whiteboard design of a three server web infrastructure that hosts the website the `www.foobar.com`. Captures:
- 3 servers
- 2 web server (Nginx)
- 2 application servers
- 1 load-balancer (HAproxy)
- 2 set of application files (the code base)
- 2 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

**2. Secured and monitored web infrastructure** `[2-secured_and_monitored_web_infrastructure]` >> Whiteboard design of a three server web infrastructure that hosts the website the `www.foobar.com`, that is secured and the serve traffic encrypted and monitored. Captures:
- 3 servers
- 3 firewalls
- 2 web server (Nginx)
- 2 application servers
- 1 load-balancer (HAproxy)
- 2 set of application files (the code base)
- 2 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
- 1 SSL certificate to serve `www.foobar.com` over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)

**3. Scale up** `[3-scale_up]` >> Whiteboard design of a three server web infrastr    ucture that hosts the website the `www.foobar.com`, that is secured and the serve traffic encrypted and monitored. Captures:
- 4 servers
- 3 firewalls
- 2 web server (Nginx)
- 2 application servers
- 2 load-balancers (HAproxy) configured as cluster with the other one
- 2 set of application files (the code base)
- 2 database (MySQL)
- 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
- 1 SSL certificate to serve `www.foobar.com` over HTTPS
- 3 monitoring clients (data collector for Sumologic or other monitoring services)
- Split components (web server, application server, database) with their own server
