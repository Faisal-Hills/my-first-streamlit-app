import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Analyst Learning Portal",
    page_icon="🎓",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("📚 Learning Modules")
page = st.sidebar.radio(
    "Choose a Topic:",
    ["🏠 Home", "🐍 Python Tutorials", "📊 Power BI Guides", "🗄️ SQL Fundamentals"]
)

# ---------------------------------------------------------
# 🏠 HOME PAGE
# ---------------------------------------------------------
if page == "🏠 Home":
    st.title("🎓 Welcome to the Analyst Learning Portal")
    st.write("This portal provides hands-on tutorials and training materials for modern data analysts. Select a module from the sidebar to begin.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🐍 Python")
        st.write("Automate workflows, manipulate data with Pandas, and build interactive web apps.")
    with col2:
        st.subheader("📊 Power BI")
        st.write("Master DAX measures, create star-schema data models, and design executive reports.")
    with col3:
        st.subheader("🗄️ SQL")
        st.write("Query relational databases, structure analytical joins, and aggregate large datasets.")

# ---------------------------------------------------------
# 🐍 PYTHON TUTORIALS
# ---------------------------------------------------------
elif page == "🐍 Python Tutorials":
    st.title("🐍 Python for Data Analytics")
    st.write("Essential Python patterns and automation scripts.")

    tab1, tab2 = st.tabs(["Conditional Logic", "Working with APIs"])

    with tab1:
        st.subheader("Interactive Grade Evaluator")
        marks = st.number_input("Enter Score (0-100):", min_value=0, max_value=100, value=78)
        
        if st.button("Calculate Grade"):
            if marks >= 95:
                st.success("Result: Grade A")
            elif marks >= 80:
                st.info("Result: Grade B")
            elif marks >= 50:
                st.warning("Result: Pass")
            else:
                st.error("Result: Fail")
        
        st.markdown("#### Sample Python Code:")
        st.code("""
marks = int(input("Enter marks: "))
if marks >= 95:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")
        """, language="python")

    with tab2:
        st.subheader("Calling a Web API")
        st.write("Use the `requests` library to fetch data from web endpoints.")
        
        st.code("""
import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Setup:", data["setup"])
    print("Punchline:", data["punchline"])
        """, language="python")

# ---------------------------------------------------------
# 📊 POWER BI GUIDES
# ---------------------------------------------------------
elif page == "📊 Power BI Guides":
    st.title("📊 Power BI & DAX Essentials")
    st.write("Best practices for report building and data modeling.")

    st.subheader("1. Core DAX Measures")
    st.markdown("""
    * **Year-to-Date (YTD) Sales:**
    ```dax
    Total Sales YTD = TOTALYTD(SUM(FactSales[Amount]), DimDate[Date])
    ```
    * **Year-over-Year (YoY) Growth %:**
    ```dax
    YoY Growth % = 
    VAR PreviousYear = CALCULATE(SUM(FactSales[Amount]), SAMEPERIODLASTYEAR(DimDate[Date]))
    VAR CurrentYear = SUM(FactSales[Amount])
    RETURN 
    DIVIDE(CurrentYear - PreviousYear, PreviousYear, 0)
    ```
    """)

    st.subheader("2. Modeling Best Practices")
    st.info("💡 Tip: Always organize your model into a Star Schema with one-to-many (`1:*`) relationships pointing from Dimension tables to Fact tables.")

# ---------------------------------------------------------
# 🗄️ SQL FUNDAMENTALS
# ---------------------------------------------------------
elif page == "🗄️ SQL Fundamentals":
    st.title("🗄️ SQL Querying Reference")
    st.write("A quick cheat-sheet for common database operations.")

    st.subheader("Common Analytical Queries")
    st.markdown("""
    * **Top Records & Filtering:**
    ```sql
    SELECT TOP 10 
        ProductID, 
        ProductName 
    FROM Products 
    WHERE IsDiscontinued = 0;
    ```
    * **Aggregations with GROUP BY:**
    ```sql
    SELECT 
        Department, 
        COUNT(EmployeeID) AS TotalEmployees,
        AVG(Salary) AS AverageSalary
    FROM Employees
    GROUP BY Department
    HAVING COUNT(EmployeeID) > 5;
    ```
    """)
