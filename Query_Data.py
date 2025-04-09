
import pandas as pd
from Clickhouse import client

def query_from_clickhouse():
    query = """
    SELECT timestamp, line, status
    FROM tfl_status
    ORDER BY timestamp DESC
    LIMIT 100
    """
    result = client.query(query).result_rows
    return pd.DataFrame(result, columns=['timestamp', 'line', 'status'])
