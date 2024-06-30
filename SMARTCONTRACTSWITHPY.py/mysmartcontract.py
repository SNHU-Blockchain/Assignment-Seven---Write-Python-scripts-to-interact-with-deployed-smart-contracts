from web3 import Web3
from solcx import compile_source

# Connect to the local Ethereum node
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Solidity source code
contract_source_code = '''
pragma solidity ^0.5.0;

contract SimpleStorage {
    uint public storedData;

    constructor(uint initVal) public {
        storedData = initVal;
    }

    function set(uint x) public {
        storedData = x;
    }

    function get() public view returns (uint) {
        return storedData;
    }
}
'''

# Compile the contract
compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:SimpleStorage']

# Deploy the contract
SimpleStorage = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = SimpleStorage.constructor(42).transact({'from': w3.eth.accounts[0]})
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Get the contract instance
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])

# Interact with the contract
print(simple_storage.functions.get().call())  # Should print 42
simple_storage.functions.set(100).transact({'from': w3.eth.accounts[0]})
print(simple_storage.functions.get().call())  # Should print 100
