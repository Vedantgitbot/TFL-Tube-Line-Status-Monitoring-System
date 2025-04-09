import clickhouse_connect

# Set up ClickHouse client
client = clickhouse_connect.get_client(
    host='localhost',  # Adjust if ClickHouse is hosted elsewhere
    port=8123,         # Default ClickHouse port
    username='default',  # Adjust based on your configuration
    password=''          # Provide password if required
)

# Define the SQL query
query = """
SELECT line, status, COUNT(*) AS disruption_count
FROM tfl_status
WHERE timestamp >= '2025-04-01' AND timestamp <= '2025-04-07'
GROUP BY line, status
ORDER BY disruption_count DESC
"""

# Execute the query
try:
    result = client.query(query).result_rows

    if not result:
        print("No results found for the query.")
    else:
        # Display the result
        for row in result:
            print(row)

except Exception as e:
    print(f"Error executing query: {e}")
