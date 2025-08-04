import streamlit as st
import mysql.connector

# Database credentials
db_config = {
    "host": "82.180.143.66",
    "user": "u263681140_students",
    "password": "testStudents@123",
    "database": "u263681140_students"
}

# Title
st.title("Update F1 Column in UpdateFlag Table")

# ID selection from dropdown
selected_id = st.selectbox("Select ID to update (2 to 12):", list(range(2, 13)))

# Input for new F1 value
new_f1_value = st.text_input("Enter new value for F1:")

# Button to update database
if st.button("Update F1"):
    try:
        # Connect to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare and execute update query
        update_query = "UPDATE UpdateFlag SET F1 = %s WHERE id = %s"
        cursor.execute(update_query, (new_f1_value, selected_id))
        conn.commit()

        st.success(f"Row with ID {selected_id} updated successfully!")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
