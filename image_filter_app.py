
import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io


st.set_page_config(page_title=" Basic Image Filter App",
page_icon=":camera:"
)

# Custom CSS for a polished look
st.markdown(
    """
    <style>
        /* Customizing the main container */
        .block-container {
            padding: 2rem 3rem;  /* Add some padding */
            border-radius: 15px;  /* Rounded corners */
            background-color: #f0f0f0;  /* Soft background color */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
        }
            /* Title and header styles */
        /* Sidebar customization */
        .sidebar .sidebar-content {
            background-color: #4a4a4a;
            color: #ffffff;
        }

        /* Upload button style */
        .stFileUploader {
            font-size: 1rem;
            background-color: #1e90ff;
            color: white;
            border-radius: 5px;
            padding: 0.75rem 1.25rem;
            margin-top: 1rem;
        }
        /* Buttons style 
        .stButton {
            color: #e64a19;
            border-radius: 5px;
            font-size: 1rem;
            padding: 0.75rem 1.5rem;
        }*/
        /* Filter options style */
        .stRadio {
            font-size: 1.1rem;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("Basic Image Filter App")
st.write("Upload an image and apply filters to enhance it.")


is_image_edited = False

st.sidebar.header("Filter Options")

uploaded_image = st.file_uploader(label="Upload an image", type=['jpg', 'png', 'jpeg'])


if uploaded_image:
    # Load the image
    image = Image.open(uploaded_image)
    st.image(image=image, caption="original Image", use_column_width=True)

    # Filter Options
    options = ["None", "Grayscale", "Invert Colors", "Brightness Adjustment"]
    filter_options = st.sidebar.radio(label="Choose a filter to apply", options=options)


    # Grayscale
    if filter_options == "Grayscale":
        is_image_edited = True
        filtered_image = ImageOps.grayscale(image)
        st.image(filtered_image, caption="Grayscale Image", use_column_width=True)


    # Invert Colors
    elif filter_options == "Invert Colors":
        is_image_edited = True
        # filtered_image = ImageOps.invert(image)
        filtered_image = ImageOps.invert(
            ImageOps.autocontrast((image.convert("RGB")))
        )
        st.image(filtered_image, caption="Inverted Image", use_column_width=True)


    # Brightness Adjustment
    elif filter_options == "Brightness Adjustment":
        is_image_edited = True
        brightness = st.sidebar.slider(label="Adjust Brightness", min_value=0.5, max_value=2.0, value=1.0, step=0.01)
        enhancer = ImageEnhance.Brightness(image)
        filtered_image = enhancer.enhance(brightness)
        st.image(filtered_image, caption="Brightness Adjusted Image", use_column_width=True)

    
    # Download the edited image
    if is_image_edited:
        if st.button(label="Click to download filtered image"):
            img_byte_arr = io.BytesIO()
            filtered_image.save(img_byte_arr, format="PNG")
            img_byte_arr = img_byte_arr.getvalue()
            
            st.download_button(
                label="Download Image",
                data=img_byte_arr,
                file_name="filtered_image.png",
                mime="image/png"
            )

else:
    st.write("Upload an image to begin")
