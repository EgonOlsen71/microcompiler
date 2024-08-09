# add this to compiled code:

import struct

# replace this in compiled code:

def SYSCALL(addr):
    global _memory
    global VAR_S
    global VAR_E
    global VAR_N_STRVAR
    if addr=="$ffd8()":
        submem = _memory[int(VAR_S):int(VAR_E)+1]
		
        data = b''.join(struct.pack('c', i.to_bytes(1, byteorder='big')) for i in [int(VAR_S) & 255, int(VAR_S/256)])
        data += b''.join(struct.pack('c', i.to_bytes(1, byteorder='big') if i is not None else 0) for i in submem)

        with open(VAR_N_STRVAR, 'wb') as file:
            file.write(data)