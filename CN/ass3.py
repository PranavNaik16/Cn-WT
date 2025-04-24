import ipaddress

def calculate_subnets(ip, new_prefix):
    try:
        network = ipaddress.ip_network(ip, strict=False)
        subnets = list(network.subnets(new_prefix=new_prefix))

        print(f"\nOriginal Network: {network}")
        print(f"New Subnet Mask: {subnets[0].netmask}")
        print(f"Total Subnets: {len(subnets)}")

        for i, subnet in enumerate(subnets[:5]): 
            print(f"Subnet {i + 1}: {subnet}")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage:
if __name__ == '__main__':
    ip_input = input("Enter IP address with CIDR (e.g., 192.168.1.0/24): ")
    new_prefix = int(input("Enter new subnet prefix length (e.g., 26): "))
    calculate_subnets(ip_input, new_prefix)
