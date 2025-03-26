import os

import pkg_resources
from setuptools import setup, find_packages


setup(
    name="human-eval",
    py_modules=["human-eval"],
    version="1.0",
    description="HumanEval is a benchmark for evaluating the quality of programs written by language models. It is a collection of 1000+ problems, each with a solution written by a human. The solutions are written in Python and range from simple to complex.",
    author="BragAI",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "evaluate_functional_correctness = human_eval.evaluate_functional_correctness",
        ]
    }
)
