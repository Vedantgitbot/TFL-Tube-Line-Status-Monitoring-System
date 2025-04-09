import time
from Fetch_Data import fetch_data
from Data_Insertion import insert_into_clickhouse
from Query_Data import query_from_clickhouse
from Plot_data import plot_data
import logging

logging.basicConfig(level=logging.INFO)

while True:
    try:
        start_time = time.time()

        data = fetch_data()
        if data:
            logging.info("Data fetched successfully.")
            
            insert_into_clickhouse(data)
            logging.info(f"Successfully inserted {len(data)} rows into ClickHouse.")
            
            df = query_from_clickhouse()
            
            if not df.empty:
                plot_data(df)
                logging.info("Data plotted successfully.")
            else:
                logging.warning("No data available to plot.")
        else:
            logging.warning("Failed to fetch data or received empty data.")
        
        execution_time = time.time() - start_time
        logging.info(f"Cycle completed in {execution_time:.2f} seconds. Waiting for the next iteration.")
        
        time.sleep(60)
    
    except Exception as e:
        logging.error(f"Error during the main process: {e}")
        time.sleep(60)
        
    except KeyboardInterrupt:
        logging.info("Process interrupted by user. Exiting gracefully.")
        break
