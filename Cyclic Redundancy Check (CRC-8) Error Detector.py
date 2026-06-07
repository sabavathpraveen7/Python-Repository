def calculate_crc8(data_bytes, polynomial=0x07):
    # 0x07 is a common polynomial choice for CRC-8 validation links
    crc = 0x00  # Initial register state
    
    for byte in data_bytes:
        crc ^= byte  # Bring byte into the register loop
        
        # Process each bit of the byte
        for _ in range(8):
            if crc & 0x80:  # Check if the most significant bit is set
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFF  # Keep within 8-bit limits
            
    print(f"Calculated CRC-8 Validation Byte: {hex(crc)}")
    return crc

# Verify message stream integrity
# message = b"Telemetry_Packet_A"
# calculate_crc8(message)