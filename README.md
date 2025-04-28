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

To run the implementation:

```bash
python src/main/python/research_assistant.py
```

To run it in test mode:

```bash
python src/main/python/research_assistant.py --test
```

## Testing Your Implementation

To test a specific task, run the corresponding unit test. For example:

```bash
python unittests/task_1_1_unittest.py
```

To run all tests, navigate to the `unittests` directory and run:

```bash
python -m unittest discover
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
