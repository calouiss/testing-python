import logging
logging.basicConfig(
    filename=r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\log1",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
#placeholder for timestamp :%(asctime)s
#placeholder for  level: %(levelname)s
#placeholder for message:%(message)s
)
logging.debug("Log file message")
logging.info("Log file info message")
#logging.shutdown()#Force flush to file
logging.basicConfig(level=logging.INFO)
logging.info("This is info")