import unittest
import os
import sys
from research_assistant import ResearchAssistant, load_document

class TestResearchAssistant(unittest.TestCase):
    def setUp(self):
        """Set up a research assistant and sample document for each test"""
        self.assistant = ResearchAssistant()
        self.sample_text = """
        LangChain is a framework for developing applications powered by language models.
        It enables applications that are context-aware and reason about their environment.
        The core components include models, prompts, memory, indexes, chains and agents.
        LangChain provides a standard interface for chains, lots of integrations with other tools,
        and end-to-end chains for common applications.
        """
        
        # Create a temporary sample document file for testing
        with open("temp_sample.txt", "w", encoding="utf-8") as f:
            f.write(self.sample_text)
        
    def tearDown(self):
        """Clean up temporary files after tests"""
        if os.path.exists("temp_sample.txt"):
            os.remove("temp_sample.txt")
        
    def test_load_document(self):
        """Test that document loading works correctly"""
        # Test with existing file
        loaded_text = load_document("temp_sample.txt")
        self.assertEqual(loaded_text.strip(), self.sample_text.strip())
        
        # Test with non-existent file
        error_result = load_document("nonexistent_file.txt")
        self.assertTrue(error_result.startswith("Error"))
        
    def test_document_processing(self):
        """Test that document processing works correctly"""
        result = self.assistant.process_document(self.sample_text)
        self.assertTrue("successfully" in result.lower())
        self.assertTrue(hasattr(self.assistant, 'document_chunks'))
        self.assertTrue(len(self.assistant.document_chunks) > 0)
        self.assertIsNotNone(self.assistant.vector_store)
        
    def test_question_answering_without_document(self):
        """Test behavior when asking a question without processing a document first"""
        answer = self.assistant.ask_question("What is LangChain?")
        self.assertTrue("process" in answer.lower())  # Should mention processing a document
        
    def test_question_answering(self):
        """Test that question answering works after processing a document"""
        self.assistant.process_document(self.sample_text)
        answer = self.assistant.ask_question("What is LangChain?")
        self.assertTrue(len(answer) > 0)  # We should get some answer
        
    def test_document_summarization_without_document(self):
        """Test behavior when generating a summary without processing a document first"""
        summary = self.assistant.generate_summary()
        self.assertTrue("process" in summary.lower())  # Should mention processing a document
        
    def test_document_summarization(self):
        """Test that summarization works after processing a document"""
        self.assistant.process_document(self.sample_text)
        summary = self.assistant.generate_summary()
        self.assertTrue(len(summary) > 0)  # We should get some summary
        
    def test_retrieve_relevant_chunks(self):
        """Test that document retrieval works correctly"""
        # Without document processed
        empty_chunks = self.assistant.retrieve_relevant_chunks("What are the components of LangChain?")
        self.assertEqual(len(empty_chunks), 0)  # Should get empty list
        
        # With document processed
        self.assistant.process_document(self.sample_text)
        chunks = self.assistant.retrieve_relevant_chunks("What are the components of LangChain?")
        self.assertTrue(len(chunks) > 0)  # We should get some chunks
        
# Unit tests for specific tasks in the code lab
        
class TestTask1(unittest.TestCase):
    """Tests for Task 1: Setting Up Your LangChain Environment"""
    
    def test_imports(self):
        """Test that all required libraries are imported correctly"""
        # This is a simple check to make sure all required imports are available
        try:
            from langchain.llms.fake import FakeListLLM
            from langchain.prompts import PromptTemplate
            from langchain.chains import LLMChain
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            from langchain.vectorstores import FAISS
            from langchain.embeddings import FakeEmbeddings
            from langchain.schema import Document
            import os
            self.assertTrue(True)  # If we got here, imports succeeded
        except ImportError as e:
            self.fail(f"Import error: {e}")
            
    def test_research_assistant_initialization(self):
        """Test that the ResearchAssistant class initializes correctly"""
        from research_assistant import ResearchAssistant
        
        assistant = ResearchAssistant()
        self.assertIsNotNone(assistant.llm)
        self.assertIsNone(assistant.document)
        self.assertEqual(assistant.document_chunks, [])
        self.assertIsNotNone(assistant.embeddings)
        self.assertIsNone(assistant.vector_store)
        
class TestTask2(unittest.TestCase):
    """Tests for Task 2: Document Processing and Chunking"""
    
    def setUp(self):
        from research_assistant import ResearchAssistant
        self.assistant = ResearchAssistant()
        self.sample_text = """
        LangChain is a framework for developing applications powered by language models.
        It enables applications that are context-aware and reason about their environment.
        The core components include models, prompts, memory, indexes, chains and agents.
        """
        
    def test_document_chunking(self):
        """Test that document chunking works correctly"""
        result = self.assistant.process_document(self.sample_text)
        self.assertTrue(len(self.assistant.document_chunks) > 0)
        self.assertEqual(self.assistant.document, self.sample_text)

class TestTask3(unittest.TestCase):
    """Tests for Task 3: Implementing Question Answering"""
    
    def setUp(self):
        from research_assistant import ResearchAssistant
        self.assistant = ResearchAssistant()
        self.sample_text = """
        LangChain is a framework for developing applications powered by language models.
        It enables applications that are context-aware and reason about their environment.
        The core components include models, prompts, memory, indexes, chains and agents.
        """
        self.assistant.process_document(self.sample_text)
        
    def test_retrieval(self):
        """Test that document retrieval works correctly"""
        chunks = self.assistant.retrieve_relevant_chunks("What is LangChain?")
        self.assertTrue(len(chunks) > 0)
        
    def test_question_answering(self):
        """Test that question answering works"""
        answer = self.assistant.ask_question("What is LangChain?")
        self.assertTrue(len(answer) > 0)

class TestTask4(unittest.TestCase):
    """Tests for Task 4: Document Summarization"""
    
    def setUp(self):
        from research_assistant import ResearchAssistant
        self.assistant = ResearchAssistant()
        self.sample_text = """
        LangChain is a framework for developing applications powered by language models.
        It enables applications that are context-aware and reason about their environment.
        The core components include models, prompts, memory, indexes, chains and agents.
        LangChain provides a standard interface for chains, lots of integrations with other tools,
        and end-to-end chains for common applications.
        """
        self.assistant.process_document(self.sample_text)
        
    def test_summarization(self):
        """Test that document summarization works correctly"""
        summary = self.assistant.generate_summary()
        self.assertTrue(len(summary) > 0)
        
        # Test with custom max_chunks
        summary_limited = self.assistant.generate_summary(max_chunks=1)
        self.assertTrue(len(summary_limited) > 0)
        
if __name__ == '__main__':
    unittest.main()
