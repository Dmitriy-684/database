import ipfsapi
import requests.exceptions


def ipfs_api():
    """Only works with ipfs desktop running"""
    try:
        file = input("Write your file (example.txt): ")
        ip, port = "127.0.0.1", 5001
        api = ipfsapi.Client(ip, port)
        response = api.add(file)
        print(response)
    except AttributeError:
        print('Something went wrong. Check the filename or address is correct')
        return
    try:
        api = ipfsapi.Client(ip, 8080)
        getfile = api.cat(response["Hash"]).decode("utf-8")
        print(getfile)
    except requests.exceptions.ConnectionError:
        print("Invalid address or ipfs not running")


if __name__ == "__main__":
    ipfs_api()


