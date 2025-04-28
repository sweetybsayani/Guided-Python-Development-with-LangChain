"""
Unit test for Task 1.1: Import Required Libraries
"""
import unittest
import os
import sys

# Find the correct paths based on the expected structure
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(os.path.dirname(current_dir))  # Go up to project root
src_main_python = os.path.join(base_dir, "src", "main", "python")
sys.path.append(src_main_python)

class TestRequiredLibraries(unittest.TestCase):
    def test_required_imports(self):
        """Test that all required libraries are imported correctly"""
        print("\nCHECKING TASK 1.1: REQUIRED LIBRARIES")
        print("="*50)
        
        # Print debugging info to verify paths
        print(f"Current directory: {current_dir}")
        print(f"Base directory: {base_dir}")
        print(f"Looking for python files in: {src_main_python}")
        
        # Get the path to the research_assistant.py file
        file_path = os.path.join(src_main_python, 'research_assistant.py')
        
        print(f"Checking if {file_path} exists...")
        if not os.path.exists(file_path):
            print(f"ERROR: {file_path} not found!")
            # List files in the directory to help debug
            if os.path.exists(src_main_python):
                print(f"Files found in {src_main_python}:")
                for f in os.listdir(src_main_python):
                    print(f"  - {f}")
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
