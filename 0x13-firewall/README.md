## 0x13. Firewall

**0. Block all incoming traffic but** `[0-block_all_incoming_traffic_but]` >> Bash script that installs the `ufw` firewall and setups a few rules on `web-01`.

**1. Port forwarding** `[100-port_forwarding]` >> Bash script that configures `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
