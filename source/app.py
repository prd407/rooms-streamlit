import streamlit as st

from input_files_functions import read_room_descriptions, read_attribute_dictionary
from logic_functions import get_matching_attributes, get_image_from_segmind

def room_mapping_tab(session):
    st.title("Room Mapping")
    
    room_descriptions=[]
    attribute_dict={}

    room_file = st.file_uploader("Upload room descriptions file")
    if room_file is not None:
        room_descriptions = read_room_descriptions(room_file)
        
    dict_file = st.file_uploader("Upload attribute dictionary file")
    if dict_file is not None:
        attribute_dict = read_attribute_dictionary(dict_file)
    
    if len(room_descriptions) and len(attribute_dict):
        matching_attributes = get_matching_attributes(room_descriptions, attribute_dict)

        st.write("Attributes found in the room descriptions:")
        selected_attributes = []
        for key, attribute_values in matching_attributes.items():
            current_attribute = st.selectbox(f"Select {key}", attribute_values)
            selected_attributes.append(current_attribute + f" {key}")    

        session.selected_attribute = selected_attributes
        session.tab1_done = True      

def content_generation_tab(session):
    st.title("Content Generation")
    
    if session.tab1_done:
        selected_attr = session.selected_attribute
        if selected_attr:
            selected_attr_1 = st.selectbox("Select Attribute 1", selected_attr)
            selected_attr_2 = st.selectbox("Select Attribute 2", selected_attr)
            selected_style = st.selectbox("Select Style", ["Professional", "Selfie", "Amateur"])
            
            if st.button("Generate"):
                room_description = f"A {selected_style.lower()} photo of a room having {selected_attr_1} and {selected_attr_2}"
                st.write("Generated Room Description:")
                st.write(room_description)
                placeholder = st.empty()
                placeholder.text("Calling segmind api, please wait 1-3 minutes to get response")
                img = get_image_from_segmind(room_description)
                placeholder.text("Please find the image generated below.")
                st.image(img, caption="This is generated using segmind's DvArch model.")

                session.tab2_done = True 

def main():
    st.title("Room mapping and Image generation App")
    session_state = st.session_state
    
    if 'tab1_done' not in session_state:
        session_state.tab1_done = False
    if 'tab2_done' not in session_state:
        session_state.tab2_done = False
    if 'selected_attribute' not in session_state:
        session_state.selected_attribute = None

    tabs = ["Room Mapping", "Content Generation"]
    choice = st.sidebar.selectbox("Select Tab", tabs)

    if choice == "Room Mapping":
        room_mapping_tab(session_state)
    elif choice == "Content Generation":
        content_generation_tab(session_state)

if __name__ == "__main__":
    main()
