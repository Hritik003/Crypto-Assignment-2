
# Supply chain management

## Team Members:
1. Hritik Raj
2. Kushal 
3. Supriyam Agarwal
4. Paidisetty Sai Aditya
5. Kochuri Akshay

## Routes defined:
1. /register
2. /users
3. /mine
4. /chain
5. /add/transaction
6. /list/transaction

## Steps to run:
1. CLone the repo using `https-web-url`
2. Run the app.py
3. Open post-man to run the following api calls to test:
    1. ```  
        http://127.0.0.1:5001/register  
        ```
    2. ```
        http://127.0.0.1:5001/add/transaction
        ```
    3. ```
        http://127.0.0.1:5001/mine
        ```
    4. ```
        http://127.0.0.1:5001/show/users
        ```
    5. ```
        http://127.0.0.1:5001/chain
        ```
## Sample testcase to run:
1. To register a node:
    ```json
        {
            "M1": {
                "name": "Manufacturer1",
                "type": "Manufacturer"
            },
            "d2": {
                "name": "Distributor2",
                "type": "distributor",
                "id": "D2",
                "property": ["normal-chair", "office-chair"]
            },
            "c1": {
                "name": "Client1",
                "type": "client",
                "id": "C1"
            },
        }
    ```
2. To add a new Transaction:
    ```json
    {
        "sender":"d1",
        "client":"c1",
        "product":"wood",
        "amount":20
    }
    ```
## Sample output of the blockchain:
```json
{
    "chain": [
        {
            "index": 1,
            "merkle_root": "37896e033a0c55e240d34dc05257b5210e429f802787005fdfa511ba595ceff6",
            "nonce": 157,
            "previous_hash": "c642a5c0a8580fa12c8aef88bae18a6a7864bf02444ccaa4bf156f389a6c4ea9",
            "timestamp": 1713954595.334674,
            "transactions": []
        },
        {
            "index": 2,
            "merkle_root": "65343264303538306163663239636235326537626566316262386634383237653039633661363437313439613566386539383032306130633261613830326535",
            "nonce": 46920,
            "previous_hash": "54dfde8bcd61bcc8808426521346d604b99c62369f0225417b6926666fe6867e",
            "timestamp": 1713954607.363752,
            "transactions": [
                {
                    "amount": "300",
                    "product": "wood",
                    "receiver": "c2",
                    "sender": "d1"
                }
            ]
        },
        {
            "index": 3,
            "merkle_root": null,
            "nonce": 13587,
            "previous_hash": "0000b5516a09443c2d2da3cc591460b825781dde5df424170d48fd2c0262cc9c",
            "timestamp": 1713954608.9361548,
            "transactions": []
        }
    ],
    "length": 3
}
```