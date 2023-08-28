## 0x0C. Web server

**0. Transfer a file to your server** `[0-transfer_file]` >> Bash script that transfers a file from the client to a server. The script accepts 4 parameters:
	- The path to the file to be transferred
	- The IP of the server to transfer the file to
	- The username `scp` connects with and ...
	- The path to the SSH private key that `scp` uses
Displays `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed, `scp` transfers the file to the user home directory `~/`, and strict host key checking is disabled when using `scp`.

**1. Install nginx web server** `[1-install_nginx_web_server]` >> Installing `nginx` on server `29579-web-01` and configuring it tolisten on port 80. Querying Nginx at its root `/` with a GET request (requesting a page) using `curl` returns a page that contains the string `Hello World!`. A bash script also created that configures a new Ubuntu machine to respect the stated requirements.

**2. Setup a domain name** `[2-setup_a_domain_name]` >> Setting up of a domain name with [.TECH Domains](https://get.tech/).

**3. Redirection** `[3-redirection]` >> Configuring the Nginx server so that `/redirect_me` is redirecting to another page.

**4. Not found page 404** `[4-not_found_page_404]` >> Configuring the Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`.

**5. Install Nginx web server (w/ Puppet)** `[7-puppet_install_nginx_web_server.pp]` >> Configuring the Nginx server with Puppet.
