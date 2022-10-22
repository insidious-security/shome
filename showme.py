#Author:sidious
import sys
import dns.resolver
from shodan import Shodan


def banner():
    print("""
    
███████╗██╗  ██╗ ██████╗ ██╗    ██╗███╗   ███╗███████╗
██╔════╝██║  ██║██╔═══██╗██║    ██║████╗ ████║██╔════╝
███████╗███████║██║   ██║██║ █╗ ██║██╔████╔██║█████╗  
╚════██║██╔══██║██║   ██║██║███╗██║██║╚██╔╝██║██╔══╝  
███████║██║  ██║╚██████╔╝╚███╔███╔╝██║ ╚═╝ ██║███████╗
╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚═╝     ╚═╝╚══════╝
                    -sidious-
                Type exit to quit.                                     
""")

SHODAN_API_KEY = "API-KEY-HERE"

def iplookup():
    nslook = input("Enter domain: ")
    if nslook == "exit":
        sys.exit()
    else:
        pass
    result = dns.resolver.resolve(f'{nslook}', 'A')
    for ipval in result:
        iplookup.output = ipval.to_text()

def showd():
    api = Shodan(SHODAN_API_KEY)
    host = api.host(iplookup.output)
    print("\n[IP]: {}".format(host['ip_str']))
    for item in host['data']:
        print("[Open Port]: {}".format(item['port'], item['data']))
    print("[Operating System]:",host['data'][0]['os'])
    print("[Organization]: {}".format(host.get('org')))
    print("[City]: {}".format(host.get('city')))
    print()


if __name__ == '__main__':
    banner()
    while (True):
        try:
            iplookup()
        except Exception as error:
            print("IP lookup failed.. Please check domain..!")
            continue
        except KeyboardInterrupt:
            print("\nExited by user..")
            sys.exit()
        try:
            showd()
        except Exception as error:
            print("Shodan API not available...")
    
