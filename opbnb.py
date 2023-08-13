from web3 import Web3
import time
import random
# import requests, json

w3_bnb = Web3(Web3.HTTPProvider("https://data-seed-prebsc-2-s1.bnbchain.org:8545"))
w3_opbnb = Web3(Web3.HTTPProvider("https://opbnb-testnet.nodereal.io/v1/9989d39cb7484ee9abcec2132a242315"))

### CONFIGURACIÓN ###
my_address = w3_opbnb.to_checksum_address("TU_WALLET_AQUI")
private_key = "TU_CLAVE_PRIVADA_AQUI"

second_address= w3_opbnb.to_checksum_address("TU_WALLET_SECUNDARIA_AQUI")
### ------------- ###

deposits_bnb_count = 0
withdraws_bnb_count = 0
deposits_busd_count = 0
withdraws_busd_count = 0
bnb_transfers_count = 0
busd_transfers_count = 0
mints_count = 0

busd_address = w3_opbnb.to_checksum_address("0xa9ad1484d9bfb27adbc2bf50a6e495777cc8cff2")

contract_abi_1 = [{"inputs":[{"internalType":"address payable","name":"_messenger","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"localToken","type":"address"},{"indexed":True,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeFinalized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"localToken","type":"address"},{"indexed":True,"internalType":"address","name":"remoteToken","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20BridgeInitiated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"l1Token","type":"address"},{"indexed":True,"internalType":"address","name":"l2Token","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20DepositInitiated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"l1Token","type":"address"},{"indexed":True,"internalType":"address","name":"l2Token","type":"address"},{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":False,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ERC20WithdrawalFinalized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeFinalized","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHBridgeInitiated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHDepositInitiated","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"from","type":"address"},{"indexed":True,"internalType":"address","name":"to","type":"address"},{"indexed":False,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":False,"internalType":"bytes","name":"extraData","type":"bytes"}],"name":"ETHWithdrawalFinalized","type":"event"},{"inputs":[],"name":"MESSENGER","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OTHER_BRIDGE","outputs":[{"internalType":"contract StandardBridge","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"bridgeETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositERC20To","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint32","name":"_minGasLimit","type":"uint32"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"depositETHTo","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"deposits","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_localToken","type":"address"},{"internalType":"address","name":"_remoteToken","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeERC20","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeBridgeETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_l1Token","type":"address"},{"internalType":"address","name":"_l2Token","type":"address"},{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeERC20Withdrawal","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"bytes","name":"_extraData","type":"bytes"}],"name":"finalizeETHWithdrawal","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"l2TokenBridge","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"messenger","outputs":[{"internalType":"contract CrossDomainMessenger","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]

busd_abi = [{"type":"constructor","inputs":[{"name":"_l2Bridge","type":"address","internalType":"address"},{"name":"_l1Token","type":"address","internalType":"address"}],"stateMutability":"nonpayable"},{"name":"Approval","type":"event","inputs":[{"name":"owner","type":"address","indexed":True,"internalType":"address"},{"name":"spender","type":"address","indexed":True,"internalType":"address"},{"name":"value","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False,"signature":"0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925"},{"name":"Burn","type":"event","inputs":[{"name":"_account","type":"address","indexed":True,"internalType":"address"},{"name":"_amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False,"signature":"0xcc16f5dbb4873280815c1ee09dbd06736cffcc184412cf7a71a0fdb75d397ca5"},{"name":"Mint","type":"event","inputs":[{"name":"_account","type":"address","indexed":True,"internalType":"address"},{"name":"_amount","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False,"signature":"0x0f6798a560793a54c3bcfe86a93cde1e73087d944c0ea20544137d4121396885"},{"name":"Transfer","type":"event","inputs":[{"name":"from","type":"address","indexed":True,"internalType":"address"},{"name":"to","type":"address","indexed":True,"internalType":"address"},{"name":"value","type":"uint256","indexed":False,"internalType":"uint256"}],"anonymous":False,"signature":"0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"},{"name":"allowance","type":"function","inputs":[{"name":"owner","type":"address","internalType":"address"},{"name":"spender","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"constant":True,"signature":"0xdd62ed3e","stateMutability":"view"},{"name":"approve","type":"function","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"signature":"0x095ea7b3","stateMutability":"nonpayable"},{"name":"balanceOf","type":"function","inputs":[{"name":"account","type":"address","internalType":"address"}],"outputs":[{"name":"","type":"uint256","internalType":"uint256"}],"constant":True,"signature":"0x70a08231","stateMutability":"view"},{"name":"burn","type":"function","inputs":[{"name":"_from","type":"address","internalType":"address"},{"name":"_amount","type":"uint256","internalType":"uint256"}],"outputs":[],"signature":"0x9dc29fac","stateMutability":"nonpayable"},{"name":"decimals","type":"function","inputs":[],"outputs":[{"name":"","type":"uint8","value":"18","internalType":"uint8"}],"constant":True,"signature":"0x313ce567","stateMutability":"pure"},{"name":"decreaseAllowance","type":"function","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"subtractedValue","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"signature":"0xa457c2d7","stateMutability":"nonpayable"},{"name":"increaseAllowance","type":"function","inputs":[{"name":"spender","type":"address","internalType":"address"},{"name":"addedValue","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"signature":"0x39509351","stateMutability":"nonpayable"},{"name":"l1Token","type":"function","inputs":[],"outputs":[{"name":"","type":"address","value":"0xeD24FC36d5Ee211Ea25A80239Fb8C4Cfd80f12Ee","internalType":"address"}],"constant":True,"signature":"0xc01e1bd6","stateMutability":"view"},{"name":"l2Bridge","type":"function","inputs":[],"outputs":[{"name":"","type":"address","value":"0x4200000000000000000000000000000000000010","internalType":"address"}],"constant":True,"signature":"0xae1f6aaf","stateMutability":"view"},{"name":"mint","type":"function","inputs":[{"name":"_to","type":"address","internalType":"address"},{"name":"_amount","type":"uint256","internalType":"uint256"}],"outputs":[],"signature":"0x40c10f19","stateMutability":"nonpayable"},{"name":"name","type":"function","inputs":[],"outputs":[{"name":"","type":"string","value":"Binance USD","internalType":"string"}],"constant":True,"signature":"0x06fdde03","stateMutability":"view"},{"name":"supportsInterface","type":"function","inputs":[{"name":"_interfaceId","type":"bytes4","internalType":"bytes4"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"constant":True,"signature":"0x01ffc9a7","stateMutability":"pure"},{"name":"symbol","type":"function","inputs":[],"outputs":[{"name":"","type":"string","value":"BUSD","internalType":"string"}],"constant":True,"signature":"0x95d89b41","stateMutability":"view"},{"name":"totalSupply","type":"function","inputs":[],"outputs":[{"name":"","type":"uint256","value":"440346505000000000000","internalType":"uint256"}],"constant":True,"signature":"0x18160ddd","stateMutability":"view"},{"name":"transfer","type":"function","inputs":[{"name":"recipient","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"signature":"0xa9059cbb","stateMutability":"nonpayable"},{"name":"transferFrom","type":"function","inputs":[{"name":"sender","type":"address","internalType":"address"},{"name":"recipient","type":"address","internalType":"address"},{"name":"amount","type":"uint256","internalType":"uint256"}],"outputs":[{"name":"","type":"bool","internalType":"bool"}],"signature":"0x23b872dd","stateMutability":"nonpayable"}]

mint_abi = [{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"}]


def wait(min_sec, max_sec):
	sleep_time = round( random.uniform(min_sec, max_sec) )
	print("Esperando {:,} segundos...".format(sleep_time))
	time.sleep(sleep_time)

def depositBNB():
	contract_address = w3_bnb.to_checksum_address("0x677311Fd2cCc511Bbc0f581E8d9a07B033D5E840")
	contract = w3_bnb.eth.contract(address=contract_address, abi=contract_abi_1)
	
	# Depositamos entre 0.0001 y 0.0001 bnb (de BNB Chain Testnet a opBNB Testnet)
	try:
		nonce = w3_bnb.eth.get_transaction_count(my_address)
		bnb_value = random.uniform(0.0001, 0.001)
		bnb_value = round(bnb_value, 4)

		function = contract.functions.depositETH(200000, b'')
		gas_limit = function.estimate_gas({'from': my_address}) 
		gas_price = w3_bnb.to_wei('10', 'gwei') # w3_opbnb.eth.gas_price

		tx = function.build_transaction({
			'chainId': 97,
			'gas': gas_limit,
			'gasPrice': gas_price, # w3_bnb.to_wei('10', 'gwei'),
			'nonce': nonce,
			'value': w3_bnb.to_wei(bnb_value, 'ether')
		})

		sign = w3_bnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_bnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_bnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("¡Depósito realizado correctamente! ({:.4f} BNB)".format(bnb_value))
			return True
		
		print("No se ha podido completar el depósito :(")
		return False
		
	except Exception as e:
		print("No se ha podido realizar el depósito. Error: ", e)
		return False
	
def withdrawBNB():
	contract_address = w3_opbnb.to_checksum_address("0x4200000000000000000000000000000000000010")
	bnb_value = 0.0001
	data = '0x32b7006d000000000000000000000000deaddeaddeaddeaddeaddeaddeaddeaddead000000000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000'

	try:
		tx = {
				'from': my_address,
				'to': contract_address,
				'chainId': 5611,
				'value': w3_opbnb.to_wei(bnb_value, 'ether'), 
				'nonce': w3_opbnb.eth.get_transaction_count(my_address),
				'data': data,
				'gas': 125000,
				'gasPrice': int(w3_opbnb.eth.gas_price)
			}
		sign = w3_opbnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_opbnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_opbnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("Retiro realizado correctamente!")
			return True
		
		print("No se ha podido realizar el retiro :(")
		return False
	
	except Exception as e:
		print("No se ha podido realizar el retiro. Error: ", e)
		return False
	

def depositBUSD():
	contract_address = w3_bnb.to_checksum_address("0x677311Fd2cCc511Bbc0f581E8d9a07B033D5E840")
	contract = w3_bnb.eth.contract(address=contract_address, abi=contract_abi_1)
	
	_l1Token = w3_bnb.to_checksum_address("0xeD24FC36d5Ee211Ea25A80239Fb8C4Cfd80f12Ee")
	_l2Token = w3_bnb.to_checksum_address("0xa9aD1484D9Bfb27adbc2bf50A6E495777CC8cFf2")

	try:
		nonce = w3_bnb.eth.get_transaction_count(my_address)
		busd_value = w3_bnb.to_wei(0.001, 'ether')

		function = contract.functions.depositERC20(_l1Token,_l2Token, busd_value, 200000, b'')
		gas_limit = function.estimate_gas({'from': my_address}) 
		gas_price = w3_bnb.to_wei('10', 'gwei')

		tx = function.build_transaction({
			'chainId': 97,
			'gas': gas_limit,
			'gasPrice': gas_price,
			'nonce': nonce,
		})

		sign = w3_bnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_bnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_bnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("¡Depósito de BUSD realizado correctamente!")
			return True
		
		print("No se ha podido completar el depósito de BUSD :(")
		return False
		
	except Exception as e:
		print("No se ha podido realizar el depósito de BUSD. Error: ", e)
		return False


def withdrawBUSD():
	contract_address = w3_opbnb.to_checksum_address("0x4200000000000000000000000000000000000010")
	#busd_value = w3_opbnb.to_wei(0.0001, 'ether')

	data = '0x32b7006d000000000000000000000000a9ad1484d9bfb27adbc2bf50a6e495777cc8cff200000000000000000000000000000000000000000000000000005af3107a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000800000000000000000000000000000000000000000000000000000000000000000'

	try:
		tx = {
				'from': my_address,
				'to': contract_address,
				'chainId': 5611,
				'nonce': w3_opbnb.eth.get_transaction_count(my_address),
				'data': data,
				'gas': 150000,
				'gasPrice': int(w3_opbnb.eth.gas_price)
			}
		sign = w3_opbnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_opbnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_opbnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("Retiro realizado correctamente!")
			return True
		
		print("No se han podido retirar los BUSD :(")
		return False
	
	except Exception as e:
		print("No se han podido retirar los BUSD. Error: ", e)
		return False


def transferBNB():
	try:
		nonce = w3_opbnb.eth.get_transaction_count(my_address)
		bnb_value = w3_opbnb.to_wei(0.00001, 'ether')

		gas_limit = w3_opbnb.eth.estimate_gas({
			'to': second_address,
			'value': bnb_value,
		})
		gas_price = w3_opbnb.eth.gas_price

		tx = {
			'to': second_address,
			'chainId': 5611,
			'gas': gas_limit,
			'gasPrice': gas_price, 
			'nonce': nonce,
			'value': bnb_value
		}

		sign = w3_opbnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_opbnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_opbnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("¡BNB enviado con éxito!")
			return True
		
		print("No se ha podido realizar la transferencia de BNB :(")
		return False
		
	except Exception as e:
		print("No se ha podido realizar la transferencia de BNB. Error: ", e)
		return False


def transferBUSD():
	try:
		contract = w3_opbnb.eth.contract(address=busd_address, abi=busd_abi)
		nonce = w3_opbnb.eth.get_transaction_count(my_address)
		busd_value = w3_opbnb.to_wei(0.0001, 'ether')

		function = contract.functions.transfer(second_address, busd_value)
		gas_limit = function.estimate_gas({'from': my_address}) 
		gas_price = w3_opbnb.eth.gas_price

		tx = function.build_transaction({
			'chainId': 5611,
			'gas': gas_limit,
			'gasPrice': gas_price, 
			'nonce': nonce,
		})

		sign = w3_opbnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_opbnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_opbnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("BUSD enviado con éxito!")
			return True
		
		print("No se ha podido realizar la transferencia de BUSD :(")
		return False
		
	except Exception as e:
		print("No se ha podido realizar la transferencia de BUSD. Error: ", e)
		return False


def mint():
	contract_address = w3_opbnb.to_checksum_address("0x5aee67f8dc2d9a5537d4b64057b52da31d37516b")
	try:
		contract = w3_opbnb.eth.contract(address=contract_address, abi=mint_abi)
		nonce = w3_opbnb.eth.get_transaction_count(my_address)

		function = contract.functions.mint()
		gas_limit = function.estimate_gas({'from': my_address}) 
		gas_price = w3_opbnb.eth.gas_price

		tx = function.build_transaction({
			'chainId': 5611,
			'gas': gas_limit,
			'gasPrice': gas_price, 
			'nonce': nonce,
		})

		sign = w3_opbnb.eth.account.sign_transaction(tx, private_key)
		hash_ = w3_opbnb.eth.send_raw_transaction(sign.rawTransaction)
		receipt = w3_opbnb.eth.wait_for_transaction_receipt(hash_)

		if receipt['status'] == 1:
			print("NFT minteado con éxito!")
			return True
		
		print("No se ha podido mintear el NFT :(")
		return False
		
	except Exception as e:
		print("No se ha podido mintear el NFT. Error: ", e)
		return False
	


# START

for i in range(100):
	
	if depositBNB():
		deposits_bnb_count += 1

	wait(30,60) # Hacemos una pausa de entre 30 y 60 segundos

	if depositBUSD():
		deposits_busd_count += 1

	wait(30,60)

	if transferBNB():
		bnb_transfers_count += 1
	
	wait(30,60)

	if transferBUSD():
		busd_transfers_count += 1

	wait(30,60)

	if mint():
		mints_count += 1
	
	wait(50,120)

	if withdrawBNB():
		withdraws_bnb_count += 1

	wait(30,60)

	if withdrawBUSD():
		withdraws_busd_count += 1

	wait(50,120)


print("Depósitos de BNB realizados correctamente: ", deposits_bnb_count)
print("Retiros de BNB realizados correctamente: ", withdraws_bnb_count)
print("Depósitos de BUSD realizados correctamente: ", deposits_busd_count)
print("Retiros de BUSD realizados correctamente: ", withdraws_busd_count)
print("Transferencias de BNB realizadas correctamente: ", bnb_transfers_count)
print("Transferencias de BUSD realizadas correctamente: ", busd_transfers_count)
print("Mints: ", mints_count)
