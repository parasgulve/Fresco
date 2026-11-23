import streamlit as st
from PIL import Image

import style

st.title('🎨 Fresco — Neural Style Transfer')

# File uploader for image selection
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie', 'mosaic12000', 'picasso12000', 'starrynight12000', 'cubism4000', 'cubism8000', 'cubism12000', 'abstract4000', 'abstract8000', 'eye4000', 'abstract12000', 'knifepaint4000', 'city8000', 'city12000', 'eye12000', 'floral4000', 'floral8000', 'floral12000', 'floral16000', 'neweye4000', 'eyenew8000', 'eyenew12000', 'eyenew32000', 'mosaic10k_epoch6_batchsize8', 'eyenew10k_epoch6_batchsize8', 'picasso10k_epoch6_batchsize8')
)

model = "saved_models/" + style_name + ".pth"

if uploaded_file is not None:
    # Open and convert image to RGB
    input_image = Image.open(uploaded_file).convert("RGB")
    
    st.write('### Source and Stylized Image')
    # Create three columns: left (image), middle (spacer), right (image)
    col1, spacer, col2 = st.columns([50, 2, 50])
    
    # Display the source image in the first column
    with col1:
        st.write("#### Source Image:")
        st.image(input_image, width=800)
    
    output_image = "images/output-images/" + style_name + "-" + uploaded_file.name

    clicked = st.button('Stylize')

    if clicked:
        # Save the image temporarily in RGB format
        input_image.save("temp_input_image.jpg")
        
        # Load model and apply style transfer
        model = style.load_model(model)
        style.stylize(model, "temp_input_image.jpg", output_image)

        # Display the stylized image in the third column
        with col2:
            st.write("#### Stylized Image:")
            result_image = Image.open(output_image)
            st.image(result_image, width=800)
else:
    st.write("Please upload an image to stylize.")