"""
A simplified AI Research Assistant using LangChain
"""
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

class MockLLM:
    """A simple mock LLM that returns predefined responses in sequence"""
    def __init__(self, responses):
        self.responses = responses
        self.counter = 0
    
    def invoke(self, prompt):
        """Return the next response in the sequence"""
        response = self.responses[self.counter % len(self.responses)]
        self.counter += 1
        return response

class ResearchAssistant:
    """A simple AI research assistant for processing documents and answering questions"""
    def __init__(self):
        # Initialize with mock responses
        responses = [
            "This document discusses artificial intelligence and its applications.",
            "Based on the document, machine learning is a subset of artificial intelligence.",
            "According to the document, natural language processing enables computers to understand human language.",
            "The document mentions that LangChain is a framework for developing LLM-powered applications."
        ]
        self.llm = MockLLM(responses)
        
        # Initialize document storage
        self.document = None
        self.document_chunks = []
        
    def process_document(self, document_text):
        """Process a document and prepare it for queries"""
        print(f"Processing document of length: {len(document_text)} characters")
        
        # Store the original document
        self.document = document_text
        
        # Split the document into simple chunks of 1000 characters
        self.document_chunks = []
        chunk_size = 1000
        for i in range(0, len(document_text), chunk_size):
            chunk = document_text[i:i+chunk_size]
            if chunk.strip():  # Only add non-empty chunks
                self.document_chunks.append(chunk)
        
        print(f"Document split into {len(self.document_chunks)} chunks")
        return f"Document processed successfully and split into {len(self.document_chunks)} chunks"
    
    def ask_question(self, question):
        """Ask a question about the processed document"""
        if not self.document:
            return "Please process a document first."
        
        # Retrieve the first two chunks as context
        relevant_chunks = self.document_chunks[:2] if len(self.document_chunks) >= 2 else self.document_chunks
        
        # Combine the chunks
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
        
        # Use only a subset of chunks for the summary
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

# Run this script as a demo
if __name__ == "__main__":
    import sys
    
    # Check if we should run the test automatically
    auto_run = "--test" in sys.argv
    
    print("AI Research Assistant initialized.")
    assistant = ResearchAssistant()
    
    # Automatically run with sample document in test mode
    if auto_run:
        sample_document = "sample_document.txt"
        print(f"Loading document: {sample_document}")
        document_text = load_document(sample_document)
        
        if document_text.startswith("Error"):
            print(document_text)
            sys.exit(1)
            
        print(f"Document loaded successfully! Length: {len(document_text)} characters")
        
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
        
        print("\nTest completed successfully!")
    else:
        # Interactive mode
        file_path = input("Enter the path to a document file: ")
        document_text = load_document(file_path)
        
        if document_text.startswith("Error"):
            print(document_text)
            sys.exit(1)
            
        print(f"Document loaded successfully! Length: {len(document_text)} characters")
        
        # Process the document
        result = assistant.process_document(document_text)
        print(result)
        
        # Ask a question
        question = input("\nEnter a question about the document: ")
        answer = assistant.ask_question(question)
        print(f"Answer: {answer}")
        
        # Generate summary
        print("\nGenerating document summary:")
        summary = assistant.generate_summary()
        print(f"Summary: {summary}")
