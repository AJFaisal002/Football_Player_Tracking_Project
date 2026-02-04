import streamlit as st
import os
import subprocess

st.set_page_config(page_title="Football Player Tracking", layout="wide")

st.title("⚽ Football Player Tracking & Analytics")
st.write("Upload a football video to analyze player tracking, ball possession, and movement.")

uploaded_video = st.file_uploader(
    "Upload football video",
    type=["mp4", "avi", "mov"]
)

if uploaded_video:
    input_path = "input_videos/uploaded_video.mp4"
    output_path = "output_videos/output_video.avi"

    with open(input_path, "wb") as f:
        f.write(uploaded_video.read())

    st.success("Video uploaded successfully!")

    if st.button("▶ Run Analysis"):
        with st.spinner("Processing video... This may take a few minutes."):
            subprocess.run(["python", "main.py"])

        if os.path.exists(output_path):
            st.success("Analysis completed!")

            st.video(output_path)

            with open(output_path, "rb") as f:
                st.download_button(
                    label="⬇ Download Output Video",
                    data=f,
                    file_name="football_analysis_output.avi",
                    mime="video/avi"
                )
