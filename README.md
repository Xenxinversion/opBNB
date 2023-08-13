# opBNB - THE ODYSSEY FROM TESTNET TO MAINNET

Este script hará todas las tareas de la campaña "The Odyssey from Testnet to Mainnet" por ti.

- Depositar tBNB (BNB Chain -> opBNB Chain)
- Retirar tBNB (opBNB Chain -> BNB Chain)
- Depositar tokens BEP-20 (BNB Chain -> opBNB Chain)
- Retirar tokens BEP-20 (opBNB Chain -> BNB Chain)
- Transferir tBNB (opBNB Chain)
- Transferir tokens BEP-20 (opBNB Chain)
- Mintear NFT (opBNB Chain)


## Configuración

Abre el archivo *opbnb.py* y modifica las siguientes líneas:

```python
my_address = w3_opbnb.to_checksum_address("TU_WALLET_AQUI")
private_key = "TU_CLAVE_PRIVADA_AQUI"

second_address= w3_opbnb.to_checksum_address("TU_WALLET_SECUNDARIA_AQUI")
```

***TU_WALLET_AQUI***: Sustituye este texto por la dirección de tu wallet.

***TU_CLAVE_PRIVADA_AQUI***: Sustituye este texto por la clave privada de tu wallet.

***TU_WALLET_SECUNDARIA_AQUI***: Sustituye este texto por una wallet secundaria. En esta dirección es donde recibiremos los fondos transferidos desde la wallet principal.


## Ejecución
Para ejecutar este código deberás tener Python instalado en tu computadora.

Además, necesitarás la librería web3 para que el script funcione.
Para instalarla, puedes dirigirte a la carpeta donde se encuentra el script y ejecutar el comando:
```
pip install web3
```
Para ejecutar el script, puedes dirigirte a la carpeta donde se encuentra y usar el comando:
```
python opbnb.py
```

## Información de la campaña

Puedes ver toda la información [aquí](https://opbnb.bnbchain.org/en/campaigns/the-odyssey-from-testnet-to-mainnet).

Y [aquí tienes una guía](https://www.bnbchain.org/en/blog/guide-to-completing-additional-tasks-for-the-opbnb-odyssey-from-testnet-to-mainnet-campaign/) para realizar las diferentes tareas (pero tranquilo, ¡este script lo hará por ti!)

