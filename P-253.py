
# --------------253 Proj----------------
from web3 import Web3
# Import time module here
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x0E77113879607bB3aE9eE313f253654689818B6C'
James_account = '0x210336Ba03fE62C3CED344dB1D4d76bc81248fa5'
Ryan_account  = '0xEC5478dE12db06402a59040f60c8E7651Cd06805'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei(5, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x2c1548ba008adf2d868721b3a05261226ecebf8a11da7dd188f77b3cbf6dbbb8'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
"Define the print statement and" 
print('Wait for a few seconds Transaction is in progress')
"sleep() function here"
time.sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei(15, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0xfdeda4a5f72646fb0fd11225708d30356963b1606197bfa3ca583b13f94f8594'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))



#project_253.py
#Displaying project_253.py.