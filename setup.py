from setuptools import setup, find_packages

from setuptools import setup

setup(
    name="pyspark",
    packages=['pyspark', 'pyspark.ml', 'pyspark.mllib', 'pyspark.sql', 'pyspark.streaming'],
    version="0.2.1",
)
