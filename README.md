To run: 
1. clone the repo
2. make sure you have postgres installed and a database named "payment_engine"
3. configure postgres in .env (e.g. DATABASE_URI='postgresql+psycopg2://postgres:admin@localhost:5432/payment_engine')
4. to create the tables run python create_tables.py
5. to add some initial test data to the client table run python populate_test_clients.py
6. to run the dummy payment engine run python payment_engine.py
7. it will update the client table at each run and produce the accounts.csv in the project root