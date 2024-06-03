import ntplib
from time import ctime
import os

def sync_time():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        os.system(f'date {ctime(response.tx_time)}')
        print(f"Time synchronized to {ctime(response.tx_time)}")
    except Exception as e:
        print(f"Failed to synchronize time: {e}")

sync_time()
