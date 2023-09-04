## 0x0F. Load balancer

**0. Double the number of webservers** `[0-custom_http_response_header]` >> Bash script that configures a brand new Ubuntu machine as a second web server (`web-02`) to be identical to the first (`web-01`). A custom Nginx response header (named `X-Server-By`) is added to be able to track which server is answering the HTTP requests, to understand how the load balancer works. The value of the custom HTTP header is the hostname of the server Nginx is running on. i.e. `29579-web-01` for the first and `29579-web-02` for the second.

**1. Install your load balancer** `[1-install_load_balancer]` >> Bash script that configures a new Ubuntu machine to install and configure HAproxy on the `lb-01` server, so that it sends traffic to `web-01` and `web-02`, distributes requests using a roundrobin algorithm, is managable via an init script, and the servers are configured with the right hostnames; in this case `29579-web-01` and `29579-web-02`.

**2. Add a custom HTTP header with Puppet** `[2-puppet_custom_http_response_header.pp]` >> Manifest that configures a brand new Ubuntu machine to automate the task of creating HTTP header response with Puppet. The name of the custom HTTP header is `X-Served-By`, and its value is the hostname of the server Nginx is running on.
