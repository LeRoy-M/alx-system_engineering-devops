## 0x10. HTTPS SSL

**0. World wide web** `[0-world_wide_web]` >> Bash script that configures a domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`).

**1. HAproxy SSL termination** `[1-haproxy_ssl_termination]` >> Bash script that creates a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

**2. No loophole in your website traffic** `[100-redirect_http_to_https]` >> Bash script that configures HAproxy to automatically redirect HTTP traffic to HTTPS.
