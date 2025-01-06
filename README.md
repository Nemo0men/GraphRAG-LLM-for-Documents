# GraphRAG LLM


## What is GraphRAG?

GraphRAG (Graph-based Retrieval-Augmented Generation) is a framework from Microsoft that enhances the capabilities of language models by integrating structured data from graphs. It allows the model to retrieve relevant information from a graph database and use it to generate more informed and contextually accurate responses. This approach is particularly useful in scenarios where the information is interconnected and can be better understood through relationships and nodes, such as knowledge graphs.

### How GraphRAG is Used in This Project

In this project, GraphRAG is utilized to:

- **Enhance Information Retrieval**: By leveraging graph structures, the system can retrieve more relevant and contextually appropriate data from the Chroma database.
- **Improve Response Generation**: The integration of graph-based data allows for more accurate and contextually rich responses to user queries.
- **Support Complex Queries**: GraphRAG enables the handling of complex queries that require understanding relationships between different pieces of information.

This project allows you to create a database from your documents and query it using natural language questions. Make sure to follow the steps in order to set up and use the system effectively.

## Install dependencies

1. Now run this command to install dependencies in the `requirements.txt` file. 

    ```bash
    pip install -r requirements.txt
    ```

2. Install markdown and PDF dependencies with: 

    ```bash
    pip install "unstructured[md]"
    ```

    ```bash
    pip install "unstructured[pdf]"
    ```

## Create database

Add the PDFs (or other file structures) into the `data` folder.

Create the Chroma DB.

```bash
python create_database.py
```

## Query the database

Query the Chroma DB.

```bash
python query_data.py --use-graphrag "What are the key relationships in the data?"
```

- `--use-graphrag`: This flag activates the GraphRAG functionality, allowing the system to leverage graph-based data for more informed responses.

By using the `--use-graphrag` argument, you can take advantage of the advanced capabilities of GraphRAG to handle complex queries and generate contextually rich answers.

> You'll also need to set up an OpenAI account (and set the OpenAI key in your environment variable) for this to work.

## Usage

1. **Environment Setup**: Ensure you have an OpenAI account and set your OpenAI API key in your environment variables. This is required for the query script to function properly.

    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

2. **Add Data**: Place your PDF or markdown files into the `data` directory. These files will be used to populate the database.

3. **Create Database**: Run the `create_database.py` script to process the files in the `data` directory and create a Chroma database. This step is necessary before querying.

    ```bash
    python create_database.py
    ```

4. **Query the Database**: Use the `query_data.py` script to ask questions against the database. Replace `[question]` with your actual query.

    ```bash
    python query_data.py "What is the main topic of the first chapter?"
    ```

    ```



