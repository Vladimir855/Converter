# Convertor 1 (RIPEMD160.exe)
 - Converter all possible addresses base58 to RIPEMD160 hashes for LostCoins
 - Rename your text file with addresses to **Base.txt** Output text file default RIPEMD160.txt
 - It may take more than 60 minutes to convert a database of 160,000,000 addresses and more.
 - The process of converting addresses is not fast, please wait for it to complete...

# Converter 2 (Converter.exe)
 - Converting Private key into all possible coins and base58 to RIPEMD160
 - Python version forked from [iceland2k14/coinaddress](https://github.com/iceland2k14/coinaddress)
 - The converter is intended for those who are looking for many different coins with a large base.
 - Lostcoin looks for hashes160 from all coins. If hash160 is found for Ethereum, it will give an empty legacy address.
 - You need to copy the found positive private key and add it to the converter. To find an address belonging to the found hash160. 
## Example
 ```
 C:\Users\user>Converter.exe
 Special edition of the converter for LostCoins
 Converting a Private key to all possible Coins
 Enter Private key (Ctr + V):
 cadc8edab738c1df2ce192af17e7d35ebbdcaf075e32ed2cc86f6d97c160dbae


 =========================== Private Key ==============================
 Private Key     : cadc8edab738c1df2ce192af17e7d35ebbdcaf075e32ed2cc86f6d97c160dbae
 =========================== Public Keys ==============================
 Compressed      : 03ad0831db6c686a67d03ec1087f05548b38efa2e6225dc5df317d901a312e133f
 Uncompressed    : 04ad0831db6c686a67d03ec1087f05548b38efa2e6225dc5df317d901a312e133fc766ad786abae17ec1ad30df4e410fefb81ef445f25f0c95bd03ab5a0df87193
 =========================== Hash 160 =================================
 Compressed      : 8d29c985ff7e05cb95316400a3696c20a81b3a6e
 Uncompressed    : 9335d6785440f5aea0bba4d5fa47c6077a6a5a0b
 =========================== Addresses ================================
 BTC     (Compressed)     : 1DsQLUUZ7djexxj7n43nMpGpdFkQD4d4w9
 BTC     (Uncompressed)   : 1ERNpuxsGB6ytQKTwtCSmeyBTzmyw3uQAG
 BTC     (P2SH)           : 38vv6nbRr2h9TKL9ng2iCnCQCgKgppRunM
 BTC     (Bech32 p2wpkh)  : bc1q355unp0l0czuh9f3vsq2x6tvyz5pkwnwxn0zvl
 LTC     (Compressed)     : LY6MbgnPCHyiDmRGxC35dqLaqU7gQaNVUV
 LTC     (Uncompressed)   : LYeL68GhLqM39D1d82Bk3g2wgD9G2GuSEc
 LTC     (P2SH)           : MF94Qg1Po9YaFpc3tZ242RSoXNv8qJLvXk
 LTC     (Bech32 p2wpkh)  : ltc1q355unp0l0czuh9f3vsq2x6tvyz5pkwnwz04x50
 BTG     (Compressed)     : GWiKkboW6VLx3S2QhzhtnaciYRYFDsn89t
 BTG     (Uncompressed)   : GXGJF3HpF2iGxscksprZCRK5PAZpy7Cwqe
 BTG     (P2SH)           : AP1mpjxcdH2vB7qiEE2Sw36ZXkxfapNssQ
 BTG     (Bech32 p2wpkh)  : btg1q355unp0l0czuh9f3vsq2x6tvyz5pkwnws6f8eh
 BSV     (Compressed)     : 1DsQLUUZ7djexxj7n43nMpGpdFkQD4d4w9
 BSV     (Uncompressed)   : 1ERNpuxsGB6ytQKTwtCSmeyBTzmyw3uQAG
 BTCZ    (Compressed)     : t1Wk1Loth5xXFZbn1iUruVdNjsuwUzx6rKM
 BTCZ    (Uncompressed)   : t1XHyqFP1EVtaV3NMtK1ZuU56iey4nYtWxL
 TENT    (Compressed)     : s1a59ZAyCqyo5oBhYC4u1faBTFGqedufFWK
 TENT    (Uncompressed)   : s1ad83cTWzXAQidHtMu3g5Qsp61sEKGbTsd
 DOGE    (Compressed)     : DJ1VsjRCR3dwVxuiWe3LuaSRWPUhZwMXs5
 DOGE    (Uncompressed)   : DJZUNAuWZb1GRQW4gUC1KR8nM8WHDzN7AR
 DASH    (Compressed)     : XoZFAj8T5LxF7uKhdwN1DLxcTbL6ERQwrR
 DASH    (Uncompressed)   : Xp7DfAcmDtKa3Lv3omWfdBeyJLMfzT7EUW
 SMART   (Compressed)     : SaAQNKFhqzvrVGWaKV2ruiRPH2ypzELQK2
 SMART   (Uncompressed)   : SaiNrkk1zYJBQi6vVKBXKZ7k7n1QgnZKsr
 ZCASH   (Compressed)     : t1Wk1Loth5xXFZbn1iUruVdNjsuwUzx6rKM
 ZCASH   (Uncompressed)   : t1XHyqFP1EVtaV3NMtK1ZuU56iey4nYtWxL
 ZCL     (Compressed)     : t1Wk1Loth5xXFZbn1iUruVdNjsuwUzx6rKM
 ZCL     (Uncompressed)   : t1XHyqFP1EVtaV3NMtK1ZuU56iey4nYtWxL
 ZERO    (Compressed)     : t1Wk1Loth5xXFZbn1iUruVdNjsuwUzx6rKM
 ZERO    (Uncompressed)   : t1XHyqFP1EVtaV3NMtK1ZuU56iey4nYtWxL
 ZEN     (Compressed)     : zndxKKu7AmDFGa4zedNHHG8JMnkf5djTLW8
 ZEN     (Uncompressed)   : zneWHpLbUukcbVWazoCRwfxzidVgfGyj9gX
 ZEIT    (Compressed)     : Mk7AZ1gFKqNLg4qY2T336D9wiytWUSDsRm
 ZEIT    (Uncompressed)   : Mkf93TAZUNjfbWRtCHBhW3rJZiv6FWAaZt
 Ethereum                 : 0x184b40db936addbb6968c31ed8b88533a21449f1
 ======================================================================
 Site                     : https://github.com/phrutis/LostCoins
 Donate                   : bc1qh2mvnf5fujg93mwl8pe688yucaw9sflmwsukz9
 ======================================================================
 ```
## Donation
 - BTC: bc1qh2mvnf5fujg93mwl8pe688yucaw9sflmwsukz9
## Disclaimer
ALL THE CODES, PROGRAM AND INFORMATION ARE FOR EDUCATIONAL PURPOSES ONLY. USE IT AT YOUR OWN RISK. THE DEVELOPER WILL NOT BE RESPONSIBLE FOR ANY LOSS, DAMAGE OR CLAIM ARISING FROM USING THIS PROGRAM
