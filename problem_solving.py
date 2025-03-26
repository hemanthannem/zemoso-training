class DataEncryptionSystem:
    def __init__(self):
        self.encoding_table = {}
        self.decoding_table = {}
        shift = 2 # Shift value for alphabets and numbers

        # Encoding for uppercase (A-Z) and lowercase (a-z)
        for i in range(26):
            original_upper = chr(65 + i)
            encoded_upper = chr(65 + (i + shift) % 26)
            self.encoding_table[original_upper] = encoded_upper
            self.decoding_table[encoded_upper] = original_upper

            original_lower = chr(97 + i)
            encoded_lower = chr(97 + (i + shift) % 26)
            self.encoding_table[original_lower] = encoded_lower
            self.decoding_table[encoded_lower] = original_lower

        # Encoding for digits (0-9), shifting cyclically by 3 places
        for i in range(10):
            original_digit = chr(48 + i)
            encoded_digit = chr(48 + (i + shift) % 10)
            self.encoding_table[original_digit] = encoded_digit
            self.decoding_table[encoded_digit] = original_digit

        # Encoding for spaces and newlines
        self.encoding_table[" "] = "#"
        self.encoding_table["\n"] = "@"
        self.decoding_table["#"] = " "
        self.decoding_table["@"] = "\n"

        

        
    def encode(self, message):
        """Encodes the given message using the predefined hash table."""
        encoded_message = "".join(self.encoding_table.get(char, char) for char in message)
        return encoded_message

    def decode(self, message):
        """Decodes the given message using the predefined hash table."""
        decoded_message = "".join(self.decoding_table.get(char, char) for char in message)
        return decoded_message


# Example Usage
encryption_system = DataEncryptionSystem()

message = "Ram Vemuri and Ranga Vemuri, “ MCM Layer Assignment Using Genetic Search”, Electronic Letters, vol. 30, no. 20, pp. 1635-1637, Sep 1994."
encoded = encryption_system.encode(message)
decoded = encryption_system.decode(encoded)

print(f"Original Message:\n{message}")
print(f"Encoded Message:\n{encoded}")
print(f"Decoded Message:\n{decoded}")