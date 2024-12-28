import streamlit as st
import cv2
from stream.timeconversion import timeconvert
from stream.timeextract import *
from stream.ocr_extract import *

st.title("This is sample part for demo")
upload_file = st.file_uploader("Upload a video file (MP4, AVI, MOV)", type=["mp4"])

curr_file = timeconvert(upload_file)

if curr_file:
    if 'video_time' not in st.session_state:
        st.session_state.video_time = 0
    st.video(curr_file, format='video/mp4', autoplay=True, start_time=st.session_state.video_time)

    def play_vedio(s_time=0):
        # Update the session state with the new start time
        st.session_state.video_time = s_time
        # Rerun the script to update the video playback
        st.rerun()

    start_frame = frame_extract_1(curr_file)
    end_frame = frame_extract_2(curr_file)

    # Extract timestamps from the frames
    start_time = extract_timestamp(start_frame)
    end_time = extract_timestamp(end_frame)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(f"Start Time: {start_time}")
    with col4:
        st.write(f"End Time: {end_time}")

    # Get jump time input from the user
    jump_input = st.text_input("Enter the time to jump :")
    
    def validate_time(jump):
        try:
            datetime.strptime(jump, '%I:%M:%S %p')
            return True
        except ValueError:
            return False

    if st.button("Jump to Time"):
        if validate_time(jump_input):
            jump_sec, start_sec, end_sec = jump_time(jump_input, start_time, end_time, curr_file)
            st.session_state.video_time = jump_sec
            st.rerun()



    


    
    
