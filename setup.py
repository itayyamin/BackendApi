from setuptools import setup, find_packages

setup(
    name="backendapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open("requirements.txt", "r")
        if not line.strip().startswith("#")
    ],
    python_requires=">=3.8",
    author="itayyamin",
    description="Backend API project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)