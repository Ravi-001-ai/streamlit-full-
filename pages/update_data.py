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


def update_data(student_id, field,new_value):
    query = text(f"UPDATE Student_Data SET {field} = :new_value WHERE id = :student_id")
    with engine.connect() as conn:
        conn.execute (query, {"new_value": new_value, "student_id": student_id})
        conn.commit()



st.title("update student data")
student_id = st.number_input("Enter Student ID to update", min_value=1, step = 1)
field = st.selectbox("Field to Update", ["firstname", "lastname", "titles", "age", "nationa;lity", "registration_status", "num_courses", "num_semesters"])
new_value = st.text_input("New value")
if st.button("Update"):
    try:
        update_data(student_id, field, new_value)
        st.success("Data succesfully updated!")

    except Exception as e:
        st.error(f"Error updating data: {e}")

