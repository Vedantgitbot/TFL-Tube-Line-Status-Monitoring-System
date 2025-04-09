import clickhouse_connect


client = clickhouse_connect.get_client(
    host='localhost',  
    port=8123,         
    username='default',  
    password=''          
)


query = """
SELECT line, status, COUNT(*) AS disruption_count
FROM tfl_status
WHERE timestamp >= '2025-04-01' AND timestamp <= '2025-04-07'
GROUP BY line, status
ORDER BY disruption_count DESC
"""


try:
    result = client.query(query).result_rows

    if not result:
        print("No results found for the query.")
    else:
        
        for row in result:
            print(row)

except Exception as e:
    print(f"Error executing query: {e}")
