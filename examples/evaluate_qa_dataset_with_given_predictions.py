from unitxt import get_logger
from unitxt.api import create_dataset, evaluate
from unitxt.text_utils import print_dict

logger = get_logger()

# Set up question answer pairs in a dictionary
dataset = [
    {"question": "What is the capital of Texas?", "answers": ["Austin"]},
    {"question": "What is the color of the sky?", "answers": ["Blue"]},
]

predictions = ["San Antonio", "blue"]

dataset = create_dataset(
    task="tasks.qa.open",
    test_set=dataset,
    metrics=[
        "metrics.qa.open.recommended_no_gpu",
        "metrics.qa.open.recommended_llm_as_judge",
    ],
)

evaluated_dataset = evaluate(predictions, dataset["test"])

# Print results
for instance in evaluated_dataset:
    print_dict(
        instance,
        keys_to_print=[
            "score",
        ],
    )
