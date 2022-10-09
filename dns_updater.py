from os import environ, path

import requests
from dotenv import find_dotenv, load_dotenv

ENDPOINT_UPDATE = "https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain}&password={token}"


def load_env_variables():
    global DOMAIN
    global HOST
    global TOKEN
    env_file_path = path.join(path.dirname(__file__), ".env")
    if find_dotenv(env_file_path):
        load_dotenv(env_file_path)
        print(f"Successfully loaded all the variables in {env_file_path}")
        try:
            DOMAIN = environ['namecheap_domain']
            HOST = environ['namecheap_host']
            TOKEN = environ['namecheap_ddns_token']
        except KeyError as e:
            print(f"Missing enviromental variable for: '{e.args[0]}'")
            exit(-1)
    else:
        print(f"{env_file_path} not found")
        exit(-1)


def update_dns():
    global ENDPOINT_UPDATE
    ENDPOINT_UPDATE = ENDPOINT_UPDATE.format(token=TOKEN, host=HOST, domain=DOMAIN)
    response = requests.get(ENDPOINT_UPDATE)
    if response.status_code == 200:
        print(f"Successfully updated {HOST}@{DOMAIN}")
    else:
        print(f"Error {response.status_code} while updating {HOST}@{DOMAIN}")


def main():
    load_env_variables()
    update_dns()


if __name__ == "__main__":
    main()
