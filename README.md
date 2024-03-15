# 🦜️🔗langchain-nexus

Langchain-Nexus is a versatile Python library that provides a unified interface for interacting with various language
models, allowing seamless integration and easy development with models like ChatGPT, GLM, and others.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Quick Install

With pip:

```bash
pip install langchain-nexus
```

## 🚀 How does LangChain-Nexus help?

### 📃LLM Model I/O

**ChatOpenAI:**

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_nexus import ChatOpenAI

chat = ChatOpenAI(temperature=0, openai_api_key="YOUR_API_KEY")
messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]
chat.invoke(messages)

```

**ChatZhipuAI:**

```python
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_nexus import ChatZhipuAI

chat = ChatZhipuAI(temperature=0, zhipuai_api_key="YOUR_API_KEY")
messages = [
    SystemMessage(
        content="You are a helpful assistant that translates English to French."
    ),
    HumanMessage(
        content="Translate this sentence from English to French. I love programming."
    ),
]
chat.invoke(messages)
```

### 🧬 Embedding

**OpenAIEmbeddings**

```python
from langchain_nexus import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(openai_api_key="...")

# Embed list of texts
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
len(embeddings), len(embeddings[0])

# embed_query
embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
embedded_query[:5]
```

**ZhipuAIEmbeddings**

```python
from langchain_nexus import ZhipuAIEmbeddings

embeddings_model = ZhipuAIEmbeddings(zhipuai_api_key="...")

# Embed list of texts
embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
len(embeddings), len(embeddings[0])

# embed_query
embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
embedded_query[:5]
```