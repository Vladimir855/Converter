import bit
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
from eth_hash.auto import keccak

def ETH_Address(un_pubk_bytes):
    return '0x' + keccak(un_pubk_bytes[1:])[-20:].hex()

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def hash160_to_addrbech32(hash160):
 	return pubkeyhash_to_addr_bech32(hash160, prefix='bc', witver=0, separator='1') 
print(' Special edition of the converter for LostCoins ')
print(' Converting a Private key to all possible Coins ')
print(' Enter Private key (Ctr + V):') 
hexkey = input()  
pk = bit.Key.from_hex(hexkey)
upub = pk._pk.public_key.format(compressed=False)
cpub = pk._pk.public_key.format(compressed=True)
crmd = HASH160(cpub)
urmd = HASH160(upub)
print('\n')
print(' =========================== Private Key ==============================')
print(' Private Key     :', hexkey)
print(' =========================== Public Keys ==============================')
print(' Compressed      :', cpub.hex())
print(' Uncompressed    :', upub.hex())
print(' =========================== Hash 160 =================================')
print(' Compressed      :', crmd.hex())
print(' Uncompressed    :', urmd.hex())
print(' =========================== Addresses ================================')
print(' BTC     (Compressed)     :', bit.base58.b58encode_check(b'\x00' + crmd))
print(' BTC     (Uncompressed)   :', bit.base58.b58encode_check(b'\x00' + urmd))
print(' BTC     (P2SH)           :', bit.base58.b58encode_check(b'\x05' + HASH160(b'\x00\x14' + crmd)))
print(' BTC     (Bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='bc', witver=0, separator='1'))
print(' LTC     (Compressed)     :', bit.base58.b58encode_check(b'\x30' + crmd))
print(' LTC     (Uncompressed)   :', bit.base58.b58encode_check(b'\x30' + urmd))
print(' LTC     (P2SH)           :', bit.base58.b58encode_check(b'\x32' + HASH160(b'\x00\x14' + crmd)))
print(' LTC     (Bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='ltc', witver=0, separator='1'))
print(' BTG     (Compressed)     :', bit.base58.b58encode_check(b'\x26' + crmd))
print(' BTG     (Uncompressed)   :', bit.base58.b58encode_check(b'\x26' + urmd))
print(' BTG     (P2SH)           :', bit.base58.b58encode_check(b'\x17' + HASH160(b'\x00\x14' + crmd)))
print(' BTG     (Bech32 p2wpkh)  :', pubkeyhash_to_addr_bech32(crmd, prefix='btg', witver=0, separator='1'))
print(' BSV     (Compressed)     :', bit.base58.b58encode_check(b'\x00' + crmd))
print(' BSV     (Uncompressed)   :', bit.base58.b58encode_check(b'\x00' + urmd))
print(' BTCZ    (Compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print(' BTCZ    (Uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))
print(' TENT    (Compressed)     :', bit.base58.b58encode_check(b'\x1c\x28' + crmd))
print(' TENT    (Uncompressed)   :', bit.base58.b58encode_check(b'\x1c\x28' + urmd))
print(' DOGE    (Compressed)     :', bit.base58.b58encode_check(b'\x1e' + crmd))
print(' DOGE    (Uncompressed)   :', bit.base58.b58encode_check(b'\x1e' + urmd))
print(' DASH    (Compressed)     :', bit.base58.b58encode_check(b'\x4c' + crmd))
print(' DASH    (Uncompressed)   :', bit.base58.b58encode_check(b'\x4c' + urmd))
print(' SMART   (Compressed)     :', bit.base58.b58encode_check(b'\x3f' + crmd))
print(' SMART   (Uncompressed)   :', bit.base58.b58encode_check(b'\x3f' + urmd))
print(' ZCASH   (Compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print(' ZCASH   (Uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))
print(' ZCL     (Compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print(' ZCL     (Uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))
print(' ZERO    (Compressed)     :', bit.base58.b58encode_check(b'\x1c\xb8' + crmd))
print(' ZERO    (Uncompressed)   :', bit.base58.b58encode_check(b'\x1c\xb8' + urmd))
print(' ZEN     (Compressed)     :', bit.base58.b58encode_check(b'\x20\x89' + crmd))
print(' ZEN     (Uncompressed)   :', bit.base58.b58encode_check(b'\x20\x89' + urmd))
print(' ZEIT    (Compressed)     :', bit.base58.b58encode_check(b'\x33' + crmd))
print(' ZEIT    (Uncompressed)   :', bit.base58.b58encode_check(b'\x33' + urmd))
print(' Ethereum                 :', ETH_Address(upub))
print(' ======================================================================')
print(' Site                     : https://github.com/phrutis/LostCoins       ')
print(' Donate                   : bc1qh2mvnf5fujg93mwl8pe688yucaw9sflmwsukz9 ')
print(' ======================================================================')