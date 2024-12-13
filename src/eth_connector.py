# Ethereum Connector
# This module provides functionality for interacting with Ethereum blockchain.

from web3 import Web3

class EthereumConnector:
    def __init__(self, rpc_url: str):
        """Initializes the EthereumConnector with the given RPC URL."""
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        if not self.web3.isConnected():
            raise ConnectionError("Failed to connect to Ethereum RPC.")

    def get_balance(self, address: str) -> float:
        """Fetches the balance of a given Ethereum address."""
        balance = self.web3.eth.get_balance(Web3.to_checksum_address(address))
        return self.web3.fromWei(balance, 'ether')

    def send_transaction(self, from_address: str, private_key: str, to_address: str, amount: float) -> str:
        """Sends an Ethereum transaction."""
        from_address = Web3.to_checksum_address(from_address)
        to_address = Web3.to_checksum_address(to_address)

        # Create transaction
        transaction = {
            'from': from_address,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': self.web3.eth.gas_price,
            'nonce': self.web3.eth.get_transaction_count(from_address),
        }

        # Sign transaction
        signed_tx = self.web3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Send transaction
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)
    