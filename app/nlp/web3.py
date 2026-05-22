import re
from web3 import Web3

ETH = r"0x[a-fA-F0-9]{40}"
ENS = r"[a-zA-Z0-9-]+\.eth"
TOKEN = r"\$[A-Z]{2,10}"

def detect(text):
    return {
        "wallets": re.findall(ETH, text),
        "ens": re.findall(ENS, text),
        "tokens": re.findall(TOKEN, text)
    }