import whois
import pyfiglet

art="Domain Validator"
print(pyfiglet.figlet_format(art))
print("----Developed by Ravi----")
def isregistered(domain):
    try:
        w=whois.whois(domain)
    except:
        return False
    else:
        return True,"Got Registered"

website=input("Enter a Website:")
print(isregistered(website))

if isregistered(website):
    whois_info=whois.whois(website)
    print("Domain registrar:",whois_info.registrar)
    print("WHOIS server:",whois_info.whois_server)
    print("Domain Creation Date:",whois_info.creation_date)
    print("Domain Expiration Date:",whois_info.expiration_date)