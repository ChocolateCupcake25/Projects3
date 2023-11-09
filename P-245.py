# Import web3 library
from web3 import Web3
from web3.middleware import geth_poa_middleware
from tkinter import *
root = Tk()

root.title("My Ethereum App")
root.geometry("500x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum Block", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
block_entry = Entry(root, text="This is Entry Widget", bd=2)

block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
gasused_info_label = Label(root, bg="white", font=("bold", 10))
gasused_info_label.place(relx=0.5, rely=0.38, anchor=CENTER)
gaslimit_info_label = Label(root, bg="white", font=("bold", 10))
gaslimit_info_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Write Import API url
API_url = 'https://mainnet.infura.io/v3/7ed758e089a64831b1a14bc5af650d29'
# write code to Store the url in variable
web3 = Web3.HTTPProvider(Web3(API_url))
# Write Code for Task 02 below.
def ethereum_block():
    number = int(block_entry.get())
    block_data = web3.eth.get_block()
    transaction = web3.eth.get_transaction(block_data['transaction'][-1].hex())
    value = transaction['value']
    value_in_ether = value/10**18
    value_in_usd = value_in_ether*1841.21
    # Write Code for Task 03 below.
    gas = transaction['gas']
    gasused_info_label['text']= "Value: $" + str(value_in_usd)
    gaslimit_info_label['text'] = "gas: " + str(gas)
    block_name_label['text'] = block_entry.get()

    block_entry.destroy()
    search_btn.destroy()


search_btn = Button(root, text="Search Ethereum transaction fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()

