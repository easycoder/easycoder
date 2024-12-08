from setuptools import setup, find_packages

setup(
    name="easycoder",
    version="0.3",
    packages=find_packages(),
    install_requires=[],
    author="Graham",
    author_email="gtanyware@gmail.com",
    description="EasyCoder",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/easycoder/easycoder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
