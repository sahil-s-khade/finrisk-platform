import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class ETLConfig:
    """
    ETL pipeline configuration.
    """

    NUM_TRANSACTIONS = int(
        os.getenv(
            "NUM_TRANSACTIONS",
            5000
        )
    )

    FRAUD_RATIO = float(
        os.getenv(
            "FRAUD_RATIO",
            0.05
        )
    )