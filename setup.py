from setuptools import setup, find_packages

setup(
    name="radcot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
        "openai>=1.0.0",
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.12.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Radiological Chain-of-Thought Framework for Enhanced Error Detection in Radiology Reports",
    keywords="radiology, nlp, llm, medical, error-detection",
    url="https://github.com/yourusername/radcot",
)