
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
