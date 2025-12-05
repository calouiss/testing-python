import logging
logging.basicConfig(
    filename=r"log1",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(level)s - %(message)s",
    
)
logging.info("Log file message")