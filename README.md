# Playwright Test Automation Project 
 
## Description 
Automated web testing framework using Playwright, Python and pytest 
 
## Project Structure 
- \`pages/\` - Page Object classes 
- \`tests/\` - Test cases 
- \`conftest.py\` - Pytest configuration 
- \`.gitignore\` - Git exclusion rules 
 
## Installation 
1. Clone repository: 
\`\`\`bash 
git clone https://github.com/densaburoff/PythonProjectsTests.git 
cd PythonProjectsTests 
\`\`\` 
 
2. Install dependencies: 
\`\`\`bash 
pip install playwright pytest 
playwright install 
\`\`\` 
 
## Running Tests 
\`\`\`bash 
"# Run all tests" 
pytest 
 
"# Run specific test file" 
pytest tests/my_first_test.py 
 
"# Run with detailed output" 
pytest -v 
\`\`\` 
