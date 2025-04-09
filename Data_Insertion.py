from datetime import datetime, timezone
from Clickhouse import client
import logging


logging.basicConfig(level=logging.INFO)

def insert_into_clickhouse(data):
    now = datetime.now(timezone.utc)
    rows = []
    
    for item in data:
   
        if item.get('lineStatuses'):
            for status in item['lineStatuses']:
               
                status_description = status.get('statusSeverityDescription', 'Unknown')
               
                rows.append((now, item['name'], status_description))
        else:
            logging.warning(f"Missing lineStatuses in data item: {item.get('name')}")
    
    if rows:
        try:
  
            logging.info(f"Inserting {len(rows)} rows into ClickHouse.")
            client.insert('tfl_status', rows, column_names=['timestamp', 'line', 'status'])
            logging.info("Data successfully inserted into ClickHouse.")
        except Exception as e:
            
            logging.error(f"Error inserting data into ClickHouse: {e}")
    else:
        logging.warning("No valid rows to insert into ClickHouse.")
