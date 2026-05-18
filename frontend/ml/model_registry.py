import os


MODEL_DIR = (
    "models/trained_models"
)


def get_latest_model():
    """
    Retrieve latest model version.
    """

    model_files = [

        f for f in os.listdir(MODEL_DIR)

        if f.endswith(".pkl")
    ]

    if not model_files:

        return None

    latest_model = sorted(
        model_files
    )[-1]

    return os.path.join(
        MODEL_DIR,
        latest_model
    )


if __name__ == "__main__":

    latest = get_latest_model()

    print("\nLatest Model:\n")

    print(latest)