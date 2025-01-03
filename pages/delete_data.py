import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

DB_HOST = "127.0.0.1" 
DB_PORT = "3306"  
DB_NAME = "student_database"  
DB_USER = "root"  
DB_PASSWORD = urllib.parse.quote("123456789")  


db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)


def delete_data(student_id):
    query = text("delete FROM student_data WHERE  id = :student_id")
    with engine.connect() as conn:
        conn.execute(query,{"student_id":student_id})
        conn.commit()


st.title("delete data student")
student_id = st.number_input("Enter Student ID to Delete", min_value=1, step=1)
if st.button("Delete"):
    try:
        delete_data(student_id)
        st.success(f"Data with Student ID {student_id} successfully deleted!")

    except Exception as e:
        st.error(f"Error deleting data {e}")


