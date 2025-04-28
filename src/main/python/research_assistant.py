from langchain.llms.fake import FakeListLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import FakeEmbeddings
from langchain.schema import Document
import os

class ResearchAssistant:
    def __init__(self):
        # Initialize with a mock LLM that returns predefined responses
        responses = [
            "This document discusses artificial intelligence and its applications.",
            "Based on the document, machine learning is a subset of artificial intelligence.",
            "According to the document, natural language processing enables computers to understand human language.",
            "The document mentions that LangChain is a framework for developing LLM-powered applications."
        ]
        self.llm = FakeListLLM(responses=responses)
        
        # Initialize document storage
        self.document = None
        self.document_chunks = []
        
        # Initialize the embeddings and vector store
        self.embeddings = FakeEmbeddings(size=1536)  # Using typical embedding dimension
        self.vector_store = None
    
    def process_document(self, document_text):
        """Process a document and prepare it for queries"""
        print(f"Processing document of length: {len(document_text)} characters")
        
        # Store the original document
        self.document = document_text
        
        # Create a text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        
        # Split the document into chunks
        self.document_chunks = text_splitter.split_text(document_text)
        
        print(f"Document split into {len(self.document_chunks)} chunks")
        
        # Convert text chunks to Documents with metadata
        documents = [
            Document(page_content=chunk, metadata={"chunk_id": i}) 
            for i, chunk in enumerate(self.document_chunks)
        ]
        
        # Create vector store from documents
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        
        return f"Document processed successfully and split into {len(self.document_chunks)} chunks"
    
    def retrieve_relevant_chunks(self, question, k=2):
        """Retrieve the chunks most relevant to the question"""
        if not self.vector_store:
            return []
        
        # Retrieve relevant documents from the vector store
        retrieved_docs = self.vector_store.similarity_search(question, k=k)
        
        # Extract the content from the retrieved documents
        relevant_chunks = [doc.page_content for doc in retrieved_docs]
        
        return relevant_chunks
    
    def ask_question(self, question):
        """Ask a question about the processed document"""
        if not self.document:
            return "Please process a document first."
        
        # Retrieve relevant chunks
        relevant_chunks = self.retrieve_relevant_chunks(question)
        
        if not relevant_chunks:
            return "I couldn't find relevant information to answer your question."
        
        # Combine the relevant chunks
        context = "\n\n".join(relevant_chunks)
        
        # Create a prompt template for question answering
        prompt = PromptTemplate(
            input_variables=["question", "context"],
            template="""
            Answer the question based only on the following context:
            
            Context:
            {context}
            
            Question: {question}
            
            Answer:
            """
        )
        
        # Create a chain for question answering
        chain = LLMChain(llm=self.llm, prompt=prompt)
        
        # Run the chain with the question and context
        answer = chain.run(question=question, context=context)
        
        return answer.strip()
    
    def generate_summary(self, max_chunks=3):
        """Generate a summary of the document"""
        if not self.document_chunks:
            return "Please process a document first."
        
        # For longer documents, use only a subset of chunks for the summary
        # Starting with the first chunk as it often contains the introduction
        chunks_to_summarize = self.document_chunks[:min(max_chunks, len(self.document_chunks))]
        content_to_summarize = "\n\n".join(chunks_to_summarize)
        
        # Create a prompt template for summarization
        prompt = PromptTemplate(
            input_variables=["text"],
            template="""
            Provide a concise summary of the following text. 
            Focus on the main points and key information.
            
            Text:
            {text}
            
            Summary:
            """
        )
        
        # Create a chain for summarization
        chain = LLMChain(llm=self.llm, prompt=prompt)
        
        # Generate the summary
        summary = chain.run(text=content_to_summarize)
        
        return summary.strip()

def load_document(filename):
    """Load document text from a file"""
    if not os.path.exists(filename):
        return f"Error: File {filename} not found."
        
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    
    return text

def run_cli():
    """Run the Research Assistant in command-line interface mode"""
    assistant = ResearchAssistant()
    print("AI Research Assistant initialized. Type 'exit' to quit at any time.")
    
    # Document loading
    while True:
        file_path = input("\nEnter the path to a document file: ")
        if file_path.lower() == 'exit':
            return
        
        document_text = load_document(file_path)
        if document_text.startswith("Error"):
            print(document_text)
            continue
        else:
            print(f"Document loaded successfully! Length: {len(document_text)} characters")
            break
    
    # Process the document
    result = assistant.process_document(document_text)
    print(result)
    
    # Command loop
    while True:
        print("\nWhat would you like to do?")
        print("1. Ask a question about the document")
        print("2. Generate a document summary")
        print("3. Load a different document")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            question = input("Enter your question: ")
            if question.lower() == 'exit':
                return
            answer = assistant.ask_question(question)
            print(f"\nAnswer: {answer}")
            
        elif choice == '2':
            max_chunks = input("Enter maximum number of chunks to summarize (default 3): ")
            if max_chunks.lower() == 'exit':
                return
            try:
                max_chunks = int(max_chunks) if max_chunks else 3
            except ValueError:
                print("Invalid input. Using default value of 3.")
                max_chunks = 3
            
            summary = assistant.generate_summary(max_chunks)
            print(f"\nSummary: {summary}")
            
        elif choice == '3':
            file_path = input("Enter the path to a document file: ")
            if file_path.lower() == 'exit':
                return
            
            document_text = load_document(file_path)
            if document_text.startswith("Error"):
                print(document_text)
                continue
            else:
                print(f"Document loaded successfully! Length: {len(document_text)} characters")
                result = assistant.process_document(document_text)
                print(result)
                
        elif choice == '4' or choice.lower() == 'exit':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Main execution
if __name__ == "__main__":
    import sys
    
    # Check for command line argument
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Run the test suite
        assistant = ResearchAssistant()
        print("Research Assistant initialized successfully!")
        
        # Load a document
        sample_document = "sample_document.txt"
        document_text = load_document(sample_document)
        
        if document_text.startswith("Error"):
            print(document_text)
        else:
            print(f"Document loaded successfully! Length: {len(document_text)} characters")
            print(f"Preview: {document_text[:100]}...")
            
            # Process the document
            result = assistant.process_document(document_text)
            print(result)
            
            # Test question answering
            print("\nTesting question answering:")
            test_questions = [
                "What is artificial intelligence?",
                "What is LangChain used for?",
                "How does natural language processing work?"
            ]
            
            for question in test_questions:
                print(f"\nQuestion: {question}")
                answer = assistant.ask_question(question)
                print(f"Answer: {answer}")
            
            # Test document summarization
            print("\nGenerating document summary:")
            summary = assistant.generate_summary()
            print(f"Summary: {summary}")
    else:
        # Run the CLI
        run_cli()
