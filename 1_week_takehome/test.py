from pydes import des 


class des_fault_injection(des):
    def __init__(self, fault_round=None, fault_bit_pos=None):
        super().__init__()
        self.fault_round = fault_round
        self.fault_bit_pos = fault_bit_pos

    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise ValueError("Key should be 8 bytes long")
        elif len(key) > 8:
            key = key[:8]  # Ensure key is exactly 8 bytes

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:
            raise ValueError("Data size should be multiple of 8")

        self.generatekeys()  # Generate all the keys

        text_blocks = nsplit(self.text, 8)  # Split the text into 8-byte blocks
        result = list()
        for block in text_blocks:
            block = string_to_bit_array(block)  # Convert the block to a bit array
            block = self.permut(block, PI)  # Apply the initial permutation

            g, d = nsplit(block, 32)  # Split block into left (g) and right (d) halves

            for i in range(16):  # Perform 16 rounds
                if i == self.fault_round and self.fault_bit_pos is not None:
                    # Introduce fault by flipping a specific bit
                    if self.fault_bit_pos < 32:
                        g[self.fault_bit_pos] ^= 1
                    else:
                        d[self.fault_bit_pos - 32] ^= 1

                d_e = self.expand(d, E)  # Expand d to match Ki size (48bits)
                tmp = self.xor(self.keys[i], d_e)
                tmp = self.substitute(tmp)  # Apply the SBOX substitution
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp

            result += self.permut(d + g, PI_1)  # Apply the final permutation

        final_result = bit_array_to_string(result)
        return final_result if action == ENCRYPT else self.removePadding(final_result)


# Example usage
if __name__ == "__main__":
    key = "secret_k"
    plaintext = "Hello wo"
    fault_round = 14  # Inject fault at 15th round (0-indexed, so 14)
    fault_bit_pos = 13  # Example bit position for fault injection

    des_fi = des_fault_injection(fault_round=fault_round, fault_bit_pos=fault_bit_pos)
    des = des()
    encrypted_with_fault = des_fi.encrypt(key, plaintext)
    encrypted_without_fault = des.encrypt(key, plaintext)
    print(f"Encrypted text with fault injection: {encrypted_with_fault}")
    print(f"Encrypted text without fault injection: {encrypted_without_fault}")
