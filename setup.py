from setuptools import setup, find_packages

setup(
    name="remember_me",
    version="1.0.0",
    description="A GRE vocabulary practice tool with AI assistance",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Yanxin Peng",
    author_email="peterpen@usc.edu",
    url="https://github.com/your_username/remember_me",  # Update with your GitHub repository
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
        "colorama>=0.4.6",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "remember_me=remember_me.vocab_practice:main",
        ],
    },
)