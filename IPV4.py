import ipaddress

class IPv4:
    def __init__(self, address: str):
        self.address = address

    def isValid(self) -> bool:
        """Ověřuje, zda je IP adresa platná."""
        try:
            ipaddress.IPv4Address(self.address)
            return True
        except ipaddress.AddressValueError:
            return False

    def get_broadcast(self, prefix_length: int) -> str:
        """Vrací broadcast adresu pro danou IP a prefix délku."""
        try:
            network = ipaddress.IPv4Network(f"{self.address}/{prefix_length}", strict=False)
            return str(network.broadcast_address)
        except ValueError:
            return "Neplatná síťová adresa nebo prefix."

    def checkprefix(self, prefix_length: int) -> bool:
        """Kontroluje, zda je zadaná IP adresa platná pro daný prefix."""
        try:
            network = ipaddress.IPv4Network(f"{self.address}/{prefix_length}", strict=False)
            return self.address == str(network.network_address)
        except ValueError:
            return False

    def get_ip_range(self, prefix_length: int) -> tuple:
        """Vrací rozsah IP adres v síti jako (první IP, poslední IP)."""
        try:
            network = ipaddress.IPv4Network(f"{self.address}/{prefix_length}", strict=False)
            return (str(network.network_address + 1), str(network.broadcast_address - 1))
        except ValueError:
            return ("Neplatná síťová adresa nebo prefix.",)

ip = IPv4("192.168.1.1")
print(ip.isValid())        
print(ip.get_broadcast(24))  
print(ip.checkprefix(24))    
print(ip.get_ip_range(24))   
