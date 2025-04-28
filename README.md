# Guided-Python-Development-with-LangChain
# Code Lab: Building an AI Research Assistant with LangChain

This repository contains the files for the "Guided: Building an AI Research Assistant with LangChain" code lab. In this lab, you'll build an AI research assistant using Python and LangChain that can process documents, answer questions about their content, and generate summaries.

## Prerequisites

Before starting this lab, make sure you have:

- Python 3.10 or higher installed
- Basic knowledge of Python syntax and functions
- Understanding of programming concepts like functions and conditionals
- Familiarity with simple data structures like lists and dictionaries

## File Structure

```
├── src/
│   ├── main/
│   │   └── python/
│   │       ├── research_assistant.py         # Main file for implementing your code
│   │       └── sample_document.txt           # Sample document for testing
│   │       └── test_research_assistant.py
│   └── unittests/
│       ├── task_1_1_unittest.py              # Unit test for Task 1.1
│       ├── task_1_2_unittest.py              # Unit test for Task 1.2
│       ├── task_1_3_unittest.py              # Unit test for Task 1.3
│       ├── task_2_1_unittest.py              # Unit test for Task 2.1
│       ├── task_2_2_unittest.py              # Unit test for Task 2.2
│       ├── task_3_1_unittest.py              # Unit test for Task 3.1
│       ├── task_3_2_unittest.py              # Unit test for Task 3.2
│       ├── task_3_3_unittest.py              # Unit test for Task 3.3
│       ├── task_4_1_unittest.py              # Unit test for Task 4.1
│       ├── task_4_2_unittest.py              # Unit test for Task 4.2
│       └── task_4_3_unittest.py              # Unit test for Task 4.3
├── requirements.txt                          # Dependencies for the project
└── README.md                                 # This file
```

## Installation

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Code

GitHub cloning command for this repository:
```bash
git clone https://github.com/sweetybsayani/Guided-Python-Development-with-LangChain.git
```

Once cloned, you can navigate into the project directory with:
```bash
cd Guided-Python-Development-with-LangChain
```

To run the implementation in interactive mode:

```bash
python src/main/python/research_assistant.py
```

In interactive mode, you'll be prompted to:

- Enter the path to a document file
- Ask a question about the document
- View a generated summary of the document

## Interactive Mode Instructions

When running the implementation in interactive mode, you'll interact with the research assistant through a series of prompts. Here's what to expect:

```bash
python src/main/python/research_assistant.py
```

### Example Interaction:

1. **When you run the program, you'll see:**
   ```
   AI Research Assistant initialized.
   Enter the path to a document file:
   ```

2. **Enter the path to your document:**
   ```
   Enter the path to a document file: src/main/python/sample_document.txt
   ```

3. **The assistant will load and process the document:**
   ```
   Document loaded successfully! Length: 2491 characters
   Processing document of length: 2491 characters
   Document split into 3 chunks
   Document processed successfully and split into 3 chunks
   ```

4. **You'll then be prompted to ask a question:**
   ```
   Enter a question about the document: What is LangChain used for?
   ```

5. **The assistant will answer your question:**
   ```
   Answer: The document mentions that LangChain is a framework for developing LLM-powered applications.
   ```

6. **Finally, the assistant will automatically generate a summary:**
   ```
   Generating document summary:
   Summary: This document discusses artificial intelligence and its applications, including machine learning and natural language processing. It highlights LangChain as a framework for developing applications powered by language models, providing components like models, prompts, memory, and chains.
   ```

You can provide any document path and ask any question relevant to the document's content. The assistant will process the document, answer your question based on the document content, and generate a summary automatically.

To run it in test mode:

```bash
python src/main/python/research_assistant.py --test
```
This will:

- Load the sample document
- Process the document automatically
- Run through predefined test questions
- Generate a summary of the document
- Display all results without requiring user input

## Testing Your Implementation

To test a specific task, run the corresponding unit test. For example:

```bash
python unittests/task_1_1_unittest.py
```

## Lab Structure

This lab is divided into 4 main tasks:

1. **Setting Up Your LangChain Environment**
   - Import required libraries
   - Create the ResearchAssistant class structure
   - Write code to load and verify a document

2. **Document Processing and Chunking**
   - Implement document processing
   - Test document processing functionality

3. **Implementing Question Answering**
   - Implement the retrieval mechanism
   - Implement the question answering method
   - Test question answering functionality

4. **Document Summarization**
   - Implement the document summarization method
   - Test document summarization
   - Create a command-line interface

Follow the instructions in each task, and use the unit tests to validate your implementation.

## Notes

- This lab is designed to work offline, so we use mock LLMs and embeddings instead of real ones.
- In a production environment, you would replace the mock components with actual LLM providers like OpenAI or Hugging Face.
- The code lab guides you through implementing key LangChain concepts and patterns, which can be applied to build more sophisticated AI applications.
