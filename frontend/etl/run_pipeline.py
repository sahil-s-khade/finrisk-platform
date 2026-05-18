import subprocess
import sys

from config.logger import logger


PIPELINE_STEPS = [

    {
        "name": "Generate Transactions",
        "command": [
            sys.executable,
            "-m",
            "etl.generate_transactions"
        ]
    },

    {
        "name": "Process Transactions",
        "command": [
            sys.executable,
            "-m",
            "etl.process_transactions"
        ]
    },

    {
        "name": "Behavioral Features",
        "command": [
            sys.executable,
            "-m",
            "etl.behavioral_features"
        ]
    },

    {
    "name": "Data Quality Checks",
    "command": [
        sys.executable,
        "-m",
        "etl.data_quality_checks"
    ]
},

    {
    "name": "Fraud Risk Scoring",
    "command": [
        sys.executable,
        "-m",
        "etl.risk_scoring"
    ]
},

    {
        "name": "Load Transactions",
        "command": [
            sys.executable,
            "-m",
            "etl.load_transactions"
        ]
    }
]


def run_step(step):
    """
    Execute ETL pipeline step.
    """

    logger.info(
        f"Starting step:"
        f" {step['name']}"
    )

    try:

        result = subprocess.run(
            step["command"],
            check=True,
            capture_output=True,
            text=True
        )

        logger.info(
            f"Completed step:"
            f" {step['name']}"
        )

        logger.info(result.stdout)

    except subprocess.CalledProcessError as e:

        logger.error(
            f"Pipeline failed during:"
            f" {step['name']}"
        )

        logger.error(e.stderr)

        raise


def run_pipeline():
    """
    Execute complete ETL workflow.
    """

    logger.info(
        "\nStarting ETL pipeline execution...\n"
    )

    for step in PIPELINE_STEPS:

        run_step(step)

    logger.info(
        "\nETL pipeline completed successfully!"
    )


if __name__ == "__main__":

    run_pipeline()