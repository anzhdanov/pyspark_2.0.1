from setuptools import setup, find_packages

setup(
    name="pyspark",
    packages=['pyspark'],
    version="2.0.1",
    description="Apache spark packages for python.",
    author='Apache',
    author_email='user.spark@apache.org',
    url='https://github.com/anzhdanov/pyspark_2.0.1/',
    keywords=['apache', 'pyspark'],
    include_package_data=True,
    entry_points={},
    zip_safe=False,
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Distribute Computing ::Apache Pyspark',
    ]
)