"""
Unit test for Task 1.1: Import Required Libraries
"""
import unittest
import os
import sys

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..", "..", "python")
sys.path.append(parent_dir)

class TestRequiredLibraries(unittest.TestCase):
    def test_required_imports(self):
        """Test that all required libraries are imported correctly"""
        print("\nCHECKING TASK 1.1: REQUIRED LIBRARIES")
        print("="*50)
        
        # Get the path to the research_assistant.py file
        file_path = os.path.join(parent_dir, 'research_assistant.py')
        
        print(f"Checking if {file_path} exists...")
        if not os.path.exists(file_path):
            print(f"ERROR: {file_path} not found!")
            self.fail(f"research_assistant.py file not found. Make sure it's in the correct location.")
        else:
            print(f"File found at {file_path}")
        
        # Read the file content
        print("Reading file content...")
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Check for simplified required imports
        print("\nChecking for required library imports:")
        
        # Check PromptTemplate import
        if "from langchain.prompts import PromptTemplate" in content:
            print("✅ PromptTemplate is correctly imported from langchain.prompts")
        else:
            print("❌ ERROR: PromptTemplate is not imported correctly!")
            print("  SOLUTION: Add 'from langchain.prompts import PromptTemplate' at the top of your file")
            self.assertIn("from langchain.prompts import PromptTemplate", content,
                         "You need to import PromptTemplate from langchain.prompts")
            
        # Check LLMChain import
        if "from langchain.chains import LLMChain" in content:
            print("✅ LLMChain is correctly imported from langchain.chains")
        else:
            print("❌ ERROR: LLMChain is not imported correctly!")
            print("  SOLUTION: Add 'from langchain.chains import LLMChain' at the top of your file")
            self.assertIn("from langchain.chains import LLMChain", content,
                         "You need to import LLMChain from langchain.chains")
            
        # Check os import
        if "import os" in content:
            print("✅ os is correctly imported")
        else:
            print("❌ ERROR: os is not imported!")
            print("  SOLUTION: Add 'import os' at the top of your file")
            self.assertIn("import os", content,
                         "You need to import the os module")
        
        print("\nTASK 1.1 COMPLETE! All required libraries are correctly imported.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
