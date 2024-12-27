import os
from ravenrpc import Ravencoin
import json

# Configure RPC connection
rpc_user = "username"
rpc_password = "password"
rpc_port = 8819

# Initialize Ravencoin RPC client
client = Ravencoin(rpc_user, rpc_password, port=rpc_port)

# Read the last processed block from nonce.lst
nonce_list_file = 'nonce.lst'
start_block = 1
if os.path.exists(nonce_list_file):
    with open(nonce_list_file, 'r') as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1].strip()
            try:
                start_block = int(last_line.split(',')[0]) + 1
            except (ValueError, IndexError):
                print("Error parsing last line of nonce.lst. Starting from block 1.")

# Get the current block count
block_count = client.getblockcount()

# Loop through the blocks and fetch nonces
with open(nonce_list_file, 'a') as f:
    for block_number in range(start_block, block_count["result"] + 1):
        block_hash = client.getblockhash(block_number)
        block_data = client.getblock(block_hash["result"])
        
        #set to >= 1219736 for RVN
        nonce = block_data["result"]["nonce64"] if block_number >=0 else block_data["result"]["nonce"]

        # Write the block number and nonce to nonce.lst
        line = f"{block_number},{nonce}\n"
        f.write(line)
        print(line.strip())
