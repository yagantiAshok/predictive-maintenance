

import os 
from from_root import from_root
from datetime import datetime
import logging

LOG_FILE = f"{datetime.now().strftime('%d-%b-%y %I-%M-%p')}.log"
log_dir = "LOGS"
log_path = os.path.join(from_root(),log_dir)
os.makedirs(log_path,exist_ok=True)
log_file_path = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(name)s - %(levelname)s - %(filename)s] %(message)s",
    datefmt="%b-%d-%y %I-%M-%p",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]

)

logger = logging.getLogger(__name__)

