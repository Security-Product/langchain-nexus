import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="langchain_nexus",
    version="0.0.0",
    author="geb",
    author_email="853934146@qq.com",
    description="Langchain-Nexus is a Python library enabling easy integration with diverse language models like ChatGPT and GLM through a unified interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Security-Product/langchain-nexus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['langchain', 'openai', 'zhipuai', 'langchain-openai'],
    python_requires='>=3.10',
)
