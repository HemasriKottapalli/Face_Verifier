

---

# Face Verification Model using DeepFace

This project demonstrates a face verification system using **DeepFace**, deployed on **Hugging Face Spaces** with **Gradio**.

## Requirements

To run this project locally, make sure you have the following dependencies installed. You can find all required packages in the `requirements.txt` file.

## Setup Instructions

1. **Clone the repository**  
   Clone this project to your local machine:
   ```bash
   git clone [repository-url]
   cd [repository-folder]
   ```

2. **Create a virtual environment**  
   It's a good practice to use a virtual environment to manage dependencies. You can create one using `venv`:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**  
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**  
   Once the virtual environment is active, install the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**  
   After setting up, you can run the application:
   ```bash
   python app.py
   ```

## How It Works

- The model uses **DeepFace** for facial recognition and verification.
- It is deployed using **Gradio**, allowing you to interact with the model in real-time via a web interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

