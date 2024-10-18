# Face_Verifier - a Face Verification Model using DeepFace
Takes in two images as input and spits out if they are of the same person.

Requirements
To run this project locally, make sure you have the following dependencies installed. You can find all required packages in the requirements.txt file.

Setup Instructions
Clone the repository
Clone this project to your local machine:

bash
Copy code
git clone [repository-url]
cd [repository-folder]
Create a virtual environment
It's a good practice to use a virtual environment to manage dependencies. You can create one using venv:

bash
Copy code
python -m venv venv
Activate the virtual environment
On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies
Once the virtual environment is active, install the required packages from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Run the application
After setting up, you can run the application:

bash
Copy code
python app.py
How It Works
The model uses DeepFace for facial recognition and verification.
It is deployed using Gradio, allowing you to interact with the model in real-time via a web interface.
License
This project is licensed under the MIT License - see the LICENSE file for details.
