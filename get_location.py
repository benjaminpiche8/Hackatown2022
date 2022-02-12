# import socket
import ipinfo

# def get_ip_address() :
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#     return ip_address

def get_city_location() :
    access_token = '8132a2ee3d6aa3'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    return details.city

if __name__ == "__main__" :
    print(get_city_location())