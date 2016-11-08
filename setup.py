from setuptools import setup, find_packages

setup(
    name="pyspark",
    packages=['py4j', 'py4j.tests', 'pyspark', 'pyspark.ml', 'pyspark.ml.linalg', 'pyspark.ml.param', 'pyspark.mllib', 'pyspark.mllib.linalg', 'pyspark.mllib.stat', 'pyspark.sql', 'pyspark.streaming'],
    version="0.2.1",
)
