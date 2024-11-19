def convert_to_18_char(sf_id):
    if len(sf_id) == 18:
        return sf_id
    if len(sf_id) != 15:
        raise ValueError("Salesforce ID must be either 15 or 18 characters in length.")
    
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    def calculate_position(segment):
        position = 0
        for idx, char in enumerate(segment):
            if 'A' <= char <= 'Z':
                position += 2 ** idx
        return chars[position]

    suffix = ''.join(calculate_position(sf_id[i:i+5]) for i in range(0, 15, 5))
    
    return sf_id + suffix
    
if __name__ == "__main__":
    convert_to_18_char(input('Input Salesforce ID: "))
