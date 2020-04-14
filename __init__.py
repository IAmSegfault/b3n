def _tetrahedral(x, y, z):
    ny = x + y
    ny = ny * 0.5 * (ny + 1)
    nz = x + y + z
    mod3 = nz % 3
    if mod3 == 1:
        nz = (nz + 2) / 6 * nz * (nz + 1)
    elif mod3 == 2:
        nz = (nz + 1) / 6 * nz * (nz + 2)
    else:
        nz = nz / 6 * (nz + 1) * (nz + 2)
    return x + ny + nz


def _zn(z):
    return z < 0 and 1 - 2 * z or 2 * z


def _biject(x, y, z):
    return _tetrahedral(_zn(x), _zn(y), _zn(z))

# Map bits describes the number of bits used for x, y and z divided by 3.
# The map bits is always divided by 3 to find max position range even if you are using 2d coordinates.
# The map coordinates are always considered to be signed, adjust accordingly if you are using unsigned coordinates.


def bijection_map32(x, y, z=0, w=127, map_bits=24):
    bijection = _biject(x, y, z)
    maxmagic = int(((2**32) - 1) / 2**map_bits)
    if w > maxmagic or bijection > 2**map_bits:
        return None
    else:
        return bijection * w


def bijection_map64(x, y, z=0, w=127, map_bits=48):
    bijection = _biject(x, y, z)
    maxmagic = int(((2**64) - 1) / 2**map_bits)
    if w > maxmagic or bijection > 2**map_bits:
        return None
    else:
        return bijection * w
