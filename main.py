import streamlit as st
import langchain_helper
#Title
st.title("Restaurant Name Generator")



#Creating a side bar using streamlit
cuisine = st.sidebar.selectbox(label="Select Restaurant Type",options=["","Indian","American","Italian","Arabic","Chinese","Mexican"])

#Allowing user to add text
cuisine2 = st.sidebar.text_input(f"Enter Your Custom cuisine :")

#Creating a button to start loading
process = st.sidebar.button("Process")


#Calling LLM on click
if process:
    if cuisine or cuisine2:
        #Creating a res name and menu_items
        if cuisine:
            response = langchain_helper.get_res_details(cuisine)
            st.write(f"**{cuisine} Food Restaurant**")
        else:
            response = langchain_helper.get_res_details(cuisine2)
            st.write(f"**{cuisine2} Food Restaurant**")
        st.header(response["restaurant_name"].strip())
        menu_items = response["menu_items"].strip().split(",")
        st.write("**Menu Items**")
        for items in menu_items:
            st.write("- ",items)






