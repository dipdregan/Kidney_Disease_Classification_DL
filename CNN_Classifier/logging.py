import os
import logging
from datetime import datetime


LOG = "logs" 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

os.makedirs(LOG, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG, LOG_FILE)

logging.basicConfig(filename= LOG_FILE_PATH,
                    format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO
                    )
