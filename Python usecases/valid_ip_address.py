def check_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return "invalid"
    
    for item in parts:
        if not item.isdigit():
           return "invalid"
        
        if int(item)<0 and int(item)>255:
            return "invalid"
    return "Valid"

ip = "122.122.122.122"

print(f"The given IP address {ip} is {check_valid_ip(ip)}")