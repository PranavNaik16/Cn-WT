import socket

def dns_lookup():
    user_input = input("Enter a domain name or IP address: ").strip()

    try:

        socket.inet_aton(user_input)

        try:
            hostname = socket.gethostbyaddr(user_input)
            print(f"Reverse DNS Lookup: {user_input} → {hostname[0]}")
        except socket.herror:
            print( "No host found for this IP.")
    except socket.error:

        try:
            ip = socket.gethostbyname(user_input)
            print(f"Forward DNS Lookup: {user_input} → {ip}")
        except socket.gaierror:
            print("Invalid domain name or no internet connection.")

# Run the function
dns_lookup()
