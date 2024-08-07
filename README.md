Overview
The Document Querying App is a Streamlit-based application that allows users to upload documents, query them for specific information, maintain a history of queries, and download their chat history. The application supports documents in PDF, DOCX, and TXT formats and ensures secure storage and retrieval of data.

Features
Document Querying: Upload and query documents in PDF, DOCX, and TXT formats.
Secure Database: Secure storage of documents and user data using SQLite with encryption.
User History: Maintain and retrieve a history of user queries and responses.
Downloadable Chat History: Option to download user chat history in a readable format (TXT).
User-Friendly Interface: Clean and intuitive interface built with Streamlit.
Setup Instructions
Prerequisites
Python 3.7 or higher
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd streamlit_app
Create a Virtual Environment:

bash
Copy code
python -m venv streamlit_app_env
source streamlit_app_env/bin/activate  # On Windows use `streamlit_app_env\Scripts\activate`
Install Required Packages:

bash
Copy code
pip install -r requirements.txt
Running the Application
Run the Streamlit App:
bash
Copy code
streamlit run app.py
Usage Instructions
User Interface
Enter Your Name: Enter your name in the sidebar.
Upload Documents: Upload documents in PDF, DOCX, or TXT format using the file uploader in the sidebar.
Query Documents: Enter your query in the main input field and click the "Search" button to retrieve relevant information from the uploaded documents.
View Results: The search results will be displayed on the main page.
Download Chat History: Click the "Download Chat History" button to download your query history in a TXT format.
User History
Your queries and responses are stored securely and can be accessed and downloaded upon request.
System Architecture
Application Structure
Frontend: Built with Streamlit.
Backend: Uses SQLite for data storage.
Document Parsing: Utilizes PyPDF2 for PDFs and python-docx for DOCX files.
Database Schema
Documents Table: Stores uploaded documents with columns for id, filename, and content.
User History Table: Stores user queries and responses with columns for id, user, query, and response.
Security Measures
Data Encryption: Implemented encryption for secure data storage.
User Access Control: Each user's history is accessible only to them.
Adding New Documents
Users can upload new documents through the sidebar file uploader. The documents are parsed and stored in the database for querying.
Evaluation Criteria
Functionality
Meets Requirements: The application meets all specified requirements.
Accurate Querying: Efficient and accurate retrieval of relevant information from documents.
Security
Data Protection: Secure storage of documents and user data with encryption.
Data Integrity: Measures in place to ensure data integrity and confidentiality.
Usability
Intuitive Interface: Clean, user-friendly interface for easy navigation.
Effortless Operations: Users can easily upload documents, perform queries, view history, and download chat history.
Code Quality
Best Practices: Code is well-organized, readable, and follows best practices.
Documentation: Comprehensive documentation with clear setup instructions.
Innovation
Additional Features: Any additional features or improvements beyond the basic requirements will be positively considered.
Hosted Link
Hosted Streamlit Application
Code Repository
GitHub Repository
Contact
For any queries or issues, please contact:

Name: Sanchit Pandey
Email: sancpan02@gmail.com
