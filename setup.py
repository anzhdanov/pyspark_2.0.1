from setuptools import setup, find_packages

from setuptools import setup

setup(
    name="pyspark",
    packages=['py4j', 'pyspark', 'pyspark.ml', 'pyspark.ml.linalg', 'pyspark.ml.param', 'pyspark.mllib', 'pyspark.mllib.linalg', 'pyspark.mllib.stat', 'pyspark.sql', 'pyspark.streaming'],
    version="0.2.1",
)
