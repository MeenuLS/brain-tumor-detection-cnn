import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import pickle
import random

from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Brain Tumor Detection System",
    page_icon="🧠",
    layout="wide"
)


# ==================================================
# LOAD MODEL
# ==================================================

@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "brain_tumor_mobilenetv2_model.h5"
    )

    return model


model = load_model()


# ==================================================
# LOAD CLASS NAMES
# ==================================================

with open("class_names.pkl", "rb") as f:
    class_names = pickle.load(f)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🧠 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Prediction",
        "About Brain Tumors",
        "Model Performance"
    ]
)


# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":

    st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #000080);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
        ">
            <h1 style="color:white; margin-bottom:10px;">
                🧠 Brain Tumor Detection System
            </h1>
            <h3 style="color:white;">
                AI-Powered MRI Analysis using MobileNetV2
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        """
        This application uses a Deep Learning model
        based on MobileNetV2 Transfer Learning to
        classify brain MRI scans into:

        • Glioma

        • Meningioma

        • Pituitary Tumor

        • Healthy
        """
    )

    quotes = [

        "Early detection can improve treatment outcomes.",

        "Artificial Intelligence assists doctors but does not replace them.",

        "Regular medical consultation is essential for accurate diagnosis.",

        "MRI imaging is one of the most effective tools for detecting brain abnormalities.",

        "Technology and healthcare together can improve patient care."

    ]

    st.success(random.choice(quotes))

# ==================================================
# PREDICTION PAGE
# ==================================================

elif page == "Prediction":

    st.title("📤 Upload MRI Scan")

    uploaded_file = st.file_uploader(

        "Choose an MRI Image",

        type=["jpg", "jpeg", "png"]

    )

    if uploaded_file is not None:

        img = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:

            st.image(
                img,
                caption="Uploaded MRI Scan",
                use_container_width=True
            )

        # -----------------------------------------
        # PREPROCESS IMAGE
        # -----------------------------------------

        img_resized = img.resize((224,224))

        img_array = image.img_to_array(
            img_resized
        )

        img_array = preprocess_input(
            img_array
        )

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        # -----------------------------------------
        # PREDICT
        # -----------------------------------------

        prediction = model.predict(
            img_array,
            verbose=0
        )

        predicted_index = np.argmax(
            prediction
        )

        predicted_class = class_names[
            predicted_index
        ]

        confidence = np.max(
            prediction
        )

        with col2:

            st.subheader(
                "Prediction Result"
            )

            if predicted_class == "healthy":

                st.success(
                    "✅ Healthy Brain MRI"
                )

            else:

                st.error(
                    "⚠ Tumor Detected"
                )

            st.write(
                f"### Predicted Class: {predicted_class.capitalize()}"
            )

            st.metric(

                "Confidence Score",

                f"{confidence*100:.2f}%"
            )

        st.markdown("---")

        # -----------------------------------------
        # PROBABILITY TABLE
        # -----------------------------------------

        result_df = pd.DataFrame({

            "Class": class_names,

            "Probability":
            prediction[0]

        })

        st.subheader(
            "Prediction Probabilities"
        )

        st.dataframe(
            result_df,
            use_container_width=True
        )

       
        # -----------------------------------------
        # TUMOR DESCRIPTION
        # -----------------------------------------

        st.subheader(
            "About This Prediction"
        )

        tumor_info = {

            "glioma":
            """
            Gliomas develop from glial cells in the brain.
            They may be low-grade or highly aggressive.
            Symptoms can include headaches,
            seizures and cognitive changes.
            """,

            "meningioma":
            """
            Meningiomas originate in the membranes
            surrounding the brain and spinal cord.
            Most are slow-growing and non-cancerous.
            """,

            "pituitary":
            """
            Pituitary tumors occur in the pituitary gland.
            They may affect hormone production and
            vision.
            """,

            "healthy":
            """
            No tumor pattern was detected by the model.
            """
        }

        st.info(
            tumor_info[predicted_class]
        )

        # -----------------------------------------
        # DISCLAIMER
        # -----------------------------------------

        st.warning(
            """
            Medical Disclaimer

            This application is developed for
            educational and research purposes only.

            The prediction should NOT be considered
            a medical diagnosis.

            Please consult a qualified healthcare
            professional for proper evaluation.
            """
        )


# ==================================================
# ABOUT PAGE
# ==================================================

elif page == "About Brain Tumors":

    st.title("🧠 About Brain Tumors")

    st.markdown("""

    ## Glioma

    - Develops from glial cells.
    - Can be low-grade or aggressive.
    - May affect speech and memory.

    ## Meningioma

    - Arises from protective membranes.
    - Usually benign.
    - Often slow-growing.

    ## Pituitary Tumor

    - Occurs in pituitary gland.
    - Can affect hormones.
    - May cause vision issues.

    ## Healthy

    - No visible tumor detected.
    """)


# ==================================================
# MODEL PERFORMANCE PAGE
# ==================================================

elif page == "Model Performance":

    st.title("📊 Model Performance")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Training Accuracy",
            "92.86%"
        )

    with col2:

        st.metric(
            "Validation Accuracy",
            "89.24%"
        )

    st.info(
        """
        Model Architecture:
        MobileNetV2 Transfer Learning

        Input Size:
        224 x 224 RGB

        Optimizer:
        Adam

        Loss Function:
        Categorical Crossentropy
        """
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    """
    Developed using TensorFlow, MobileNetV2 and Streamlit

    Brain Tumor Detection using Deep Learning
    """
)