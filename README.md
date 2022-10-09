# NameCheap DNS Updater

It's a simple python script capable of updating the IP of a specific host for a domain hosted on **Namecheap**

The updated IP address is the address of the machine that made the request.

## Requirements
In order to run the script you need to install the requirements in `requirements.txt` and setup the `.env` file.

### .env file
In this file you need to have this three keys: `namecheap_ddns_token`, `namecheap_host`, `namecheap_domain`.
For further informations about these values I suggest you to visit the official [Namecheap page](https://www.namecheap.com/support/knowledgebase/article.aspx/29/11/how-to-dynamically-update-the-hosts-ip-with-an-http-request/).

## Notes
At the moment only one host update is supported