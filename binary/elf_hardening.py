from elftools.elf.elffile import ELFFile

def analyze_binary(path):
    protections = {
        "canary": False,
        "nx": False,
        "pie": False
    }

    try:
        with open(path, "rb") as f:
            elf = ELFFile(f)

            for segment in elf.iter_segments():
                if segment['p_type'] == 'PT_GNU_STACK':
                    protections["nx"] = not segment['p_flags'] & 0x1

            protections["pie"] = elf.header['e_type'] == 'ET_DYN'

    except Exception:
        pass

    return protections
