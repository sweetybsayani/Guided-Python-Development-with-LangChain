"""
Unit tests for the ResearchAssistant class
"""
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
        The core components include models, prompts, memory, chains and agents.
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
        self.assertEqual(self.assistant.document, self.sample_text)
        self.assertTrue(len(self.assistant.document_chunks) > 0)
        
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
