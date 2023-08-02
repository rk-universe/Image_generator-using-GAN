import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt



# Load your pre-trained GAN model
model = load_model('generator_model_e3d.h5')


# generate points in latent space as input for the generator
def generate_latent_points(latent_dim, n_samples):
 # generate points in the latent space
 x_input = np.random.randn(latent_dim * n_samples)
 # reshape into a batch of inputs for the network
 x_input = x_input.reshape((n_samples, latent_dim))
 return x_input


def generate_fake_samples(g_model,latent_dim,n_sample):
   sample=generate_latent_points(latent_dim, n_sample)
   x=g_model.predict(sample)
   return x

# Streamlit app
def main():
    st.title("Random Image Generator")

    if st.button("Generate"):
        # Generate a random photo using the GAN model
        image = generate_fake_samples(model, 100, 1)


                # Normalize the image data to [0.0, 1.0]
        fig, ax = plt.subplots()
        ax.imshow(image[0])
        plt.title("Generated Photo")
        plt.axis("off")
        # Display the matplotlib image in Streamlit
        # st.pyplot(fig)
        st.image(image[0],clamp=True,use_column_width=True)
if __name__ == "__main__":
    main()
