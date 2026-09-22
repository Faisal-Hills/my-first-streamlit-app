import streamlit as st
import json
import os

# 1. PAGE SETUP
st.set_page_config(
    page_title="Analyst Learning Portal",
    page_icon="🎓",
    layout="wide"
)

# Folder where your downloadable files are stored
DOCS_DIR = "documents"

# Helper function to read files for downloading
def get_file_bytes(filename):
    file_path = os.path.join(DOCS_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return None

# Load all content from the JSON file
def load_content():
    if os.path.exists("content.json"):
        with open("content.json", "r") as f:
            return json.load(f)
    return {}

data_resources = load_content()

# 2. SIDEBAR NAVIGATION
st.sidebar.title("📚 Learning Modules")
page = st.sidebar.radio(
    "Choose a Topic:",
    ["🏠 Home", "🐍 Python Tutorials", "📊 Power BI Guides", "🗄️ SQL Fundamentals"]
)

# Map sidebar pages to the keys in the JSON file
page_map = {
    "🐍 Python Tutorials": "Python",
    "📊 Power BI Guides": "PowerBI",
    "🗄️ SQL Fundamentals": "SQL"
}

# ---------------------------------------------------------
# 🏠 HOME PAGE
# ---------------------------------------------------------
if page == "🏠 Home":
    st.title("🎓 Welcome to the Analyst Learning Portal")
    st.write("An interactive hub to help you master Python, Power BI, and SQL. Select a module from the sidebar to begin.")
    
    col1, col2, col3 = st.columns(3)
    # Dynamically create the home page summary from the JSON file
    for col, key in zip([col1, col2, col3], ["Python", "PowerBI", "SQL"]):
        if key in data_resources:
            with col:
                st.subheader(f"🐍 {key}")
                st.write(data_resources[key]["description"])

# ---------------------------------------------------------
# DYNAMIC TOPIC PAGES (Python, Power BI, SQL)
# ---------------------------------------------------------
elif page in page_map:
    topic_key = page_map[page]
    
    if topic_key in data_resources:
        topic_data = data_resources[topic_key]
        
        st.title(topic_data["title"])
        st.write(topic_data["description"])
        
        tab1, tab2 = st.tabs(["🎥 Video Tutorials", "📥 Downloadable Documents"])
        
        # Render Video Tutorials Tab
        with tab1:
            if topic_data["videos"]:
                for video in topic_data["videos"]:
                    st.subheader(video["title"])
                    st.video(video["url"])
            else:
                st.info("No videos have been added to this module yet.")
                
        # Render Document Downloads Tab
        with tab2:
            st.subheader("Reference Materials")
            if topic_data["documents"]:
                for doc in topic_data["documents"]:
                    file_bytes = get_file_bytes(doc["file_name"])
                    if file_bytes:
                        mime_type = "application/pdf" if doc["type"] == "pdf" else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        st.download_button(
                            label=f"📥 {doc['label']}",
                            data=file_bytes,
                            file_name=doc["file_name"],
                            mime=mime_type
                        )
                    else:
                        st.warning(f"File not found: '{doc['file_name']}'. Please add it to the 'documents' folder.")
            else:
                st.info("No documents have been added to this module yet.")
