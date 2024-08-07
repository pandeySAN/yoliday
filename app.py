import streamlit as st
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from PyPDF2 import PdfFileReader
import docx

# Connect to database
engine = create_engine('sqlite:///documents.db')
conn = sqlite3.connect('documents.db')

# Create tables if they don't exist
conn.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    filename TEXT,
    content TEXT
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS user_history (
    id INTEGER PRIMARY KEY,
    user TEXT,
    query TEXT,
    response TEXT
)
''')
conn.close()

def read_pdf(file):
    pdf = PdfFileReader(file)
    text = ''
    for page_num in range(pdf.getNumPages()):
        text += pdf.getPage(page_num).extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def query_documents(query):
    conn = sqlite3.connect('documents.db')
    df = pd.read_sql_query(f"SELECT * FROM documents WHERE content LIKE '%{query}%'", conn)
    conn.close()
    return df

def main():
    st.title("Document Querying App")
    st.sidebar.title("Upload and Query Documents")

    user = st.sidebar.text_input("Enter your name", "")

    uploaded_file = st.sidebar.file_uploader("Upload Document", type=['pdf', 'docx', 'txt'])
    if uploaded_file is not None:
        filename = uploaded_file.name
        if filename.endswith('.pdf'):
            content = read_pdf(uploaded_file)
        elif filename.endswith('.docx'):
            content = read_docx(uploaded_file)
        else:
            content = uploaded_file.read().decode('utf-8')

        conn = sqlite3.connect('documents.db')
        conn.execute("INSERT INTO documents (filename, content) VALUES (?, ?)", (filename, content))
        conn.commit()
        conn.close()
        st.sidebar.success(f"Uploaded {filename}")

    query = st.text_input("Enter your query")
    if st.button("Search"):
        if user:
            results = query_documents(query)
            st.write(results)
            conn = sqlite3.connect('documents.db')
            conn.execute("INSERT INTO user_history (user, query, response) VALUES (?, ?, ?)", (user, query, results.to_string()))
            conn.commit()
            conn.close()
        else:
            st.error("Please enter your name")

    if st.button("Download Chat History"):
        if user:
            conn = sqlite3.connect('documents.db')
            history_df = pd.read_sql_query(f"SELECT * FROM user_history WHERE user = '{user}'", conn)
            conn.close()
            history_file = f"{user}_chat_history.txt"
            history_df.to_csv(history_file, index=False)
            with open(history_file) as f:
                st.download_button('Download Chat History', f, file_name=history_file)
        else:
            st.error("Please enter your name")

if __name__ == '__main__':
    main()
