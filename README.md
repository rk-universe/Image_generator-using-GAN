# Image Generation App using GAN on Streamlit

This Streamlit app allows you to generate new celebrity faces using a pre-trained Generative Adversarial Network (GAN) model trained on the CelebA dataset. To run the app, follow the steps below:
![Generated Celebrity Faces](sample_generated_image.png)

## Requirements

To run this app, you need to have the following Python libraries installed:

- Streamlit (`pip install streamlit`)
- TensorFlow (`pip install tensorflow`)
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

## Usage

1. Clone the repository or download the app files.

2. Make sure you have installed the required dependencies mentioned above.

3. Open a terminal or command prompt and navigate to the directory containing `app.py`.

4. Run the following command to start the Streamlit app:

```
streamlit run app.py
```

5. Once the app is running, open your web browser and go to `http://localhost:8501`.

6. Use the slider to select the number of images you want to generate, and click the "Generate" button to see the generated celebrity faces.

## Notes

- The GAN model used by the app should be trained on the CelebA dataset or a similar dataset for generating realistic celebrity-like faces.

- Ensure that the model file is saved in HDF5 format (`.h5`) for TensorFlow/Keras compatibility.

- This app provides a simple interface to generate and visualize the generated images using the GAN model.

- Remember to adapt the model loading code if your GAN model requires specific preprocessing or postprocessing steps.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- The CelebA dataset for providing the celebrity face images for training the GAN model.
- TensorFlow and Keras for their excellent machine learning frameworks.
- Streamlit for making it easy to build interactive web applications with Python.

## Contact

If you have any questions or suggestions, feel free to contact us at example@example.com.

Enjoy generating celebrity faces with GAN on Streamlit!
