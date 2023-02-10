**0. Transfer a file to your server** _[0-transfer_file]_ >> Bash script that transfers a file from the client to a server. `scp` transfers the file to the user home directory `~/`. If less than three (3) parameters pass, the following will be displayed; `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY`. The script accepts four (4) parameters:

	1. The path to the file to be transferred
	2. The IP of the server we want to transfer the file to
	3. The username `scp` connects with
	4. The path to the SSH private key that `scp` uses

**1. Install nginx web server** _[1-install_nginx_web_server]_ >> Bash script that installs `nginx` on the `web-01` server. It will be set to listen on port 80. When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it SHOULD return a page that contains the string `Hello World!`. `systemctl` should not be used to restart `nginx`.

**2. Setup a domain name** _[2-setup_a_domain_name]_ >> Created domain name provided in the file, without the subdomain e.g. `foobar.tech` and not `www.foobar.tech`. DNS records are configured with an A entry so  that the root domain points to the `web-01` IP address. The domain is entered into the `Project website url` field in the profile section of intranet. Check that the domain name is setup by verifying the Registrar here; https://whois.whoisxmlapi.com/. Should return JSON response - `"registrarName": "Dotserve Inc"`.

**3. Redirection** _[3-redirection]_ >> Nginx server configured so that `/redirect_me` redirects to another page. The redirection is to "301 Moved Permanently". Using what was done in task 1 with `1-install_nginx_web_server`, `3-redirection` is written so that it configures a brand new Ubuntu machine to the stated requirements.

**4. Not found page 404** _[4-not_found_page_404]_ >> Nginx server configured to have a custom 404 page that contains the string `Ceci n'est pas une page`. The page should return a HTTP 404 error code, contain the string `Ceci n'est pas une page`, and using what was done in task 3 with `3-redirection`, `4-not_found_page_404` is written so that it configures a brand new Ubuntu machine to the stated requirements.

**5. Install Nginx web server (w/ Puppet)** _[7-puppet_install_nginx_web_server.pp]_ >> Puppet manifest to install and configure an Nginx server instead of using a bash script. Resources to perform a 301 redirect when querying `/redirect_me` have been included in the manifest to save time and effort. Like in task 1, it will be set to list    en on port 80, and when querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it SHOULD return a page that contains the     string `Hello World!`. The redirection should also be a "301 Moved Permanently".
