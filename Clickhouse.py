import clickhouse_connect

client = clickhouse_connect.get_client(
    host='localhost',
    port=8123,
    username='default',
    password=''
)

def create_api_data_table():
    client.command('''
    CREATE TABLE IF NOT EXISTS tfl_status (
        timestamp DateTime,
        line String,
        status String
    ) ENGINE = MergeTree()
    ORDER BY timestamp;
    ''')


create_api_data_table()


print("✅ tfl_status table created or already exists.")
print(client.query("SHOW TABLES").result_rows)
