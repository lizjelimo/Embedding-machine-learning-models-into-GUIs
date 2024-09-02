# Embedding-machine-learning-models-into-GUIs
Embedding Machine Learning models into a user-friendly interface such as Streamlit for use by third party stakeholders who don't have the technical knowledge to read a Jupyter notebook.
 
## Overview
This project embeds pre-trained machine learning models into a graphical user interface (GUI) using Streamlit, allowing users to make predictions without needing technical expertise to operate complex tools like Jupyter Notebooks. This solution is containerized using Docker for easy deployment and consistent runtime environments.
 
## Features
- **User-Friendly Interface**: Simple and intuitive GUI for making predictions.
- **Pre-Trained Models**: Utilize advanced machine learning models that are ready to predict with incoming data.
- **Docker Integration**: Ensures that the application runs smoothly in any environment.
 
## Prerequisites
- Docker installed on your machine.
- Basic knowledge of Docker commands.
 
## Installation and Running
1. **Clone the Repository**
    ```bash
    git clone https://github.com/lizjelimo/Embedding-machine-learning-models-into-GUIs.git
    cd Embedding-machine-learning-models-into-GUIs
    ```
 
2. **Build the Docker Container**
    ```bash
    docker build -t ml-gui .
    ```
 
3. **Run the Application**
    ```bash
    docker run -p 8501:8501 ml-gui
    ```
 
    After running the above command, open your web browser and go to `http://localhost:8501` to access the GUI.
 
## Usage
Navigate through the GUI to upload data and make predictions using the pre-trained models. The interface is designed to be intuitive, guiding you through the process of uploading data and viewing predictions.
 
## Contributing
We welcome contributions from the community, whether it's improving the codebase, bug fixes or additional features:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your_feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your_feature`).
5. Create a new Pull Request.
 
## License
This project is available under the MIT License. See the LICENSE file for more details.
 
## Contact
If you have any questions or feedback, please contact [Liz Jelimo](mailto:jelimoliz17@gmail.com).
