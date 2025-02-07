# LLM Translation App
A streamlit-based application that leverages open-source, pretrained Large Language Models (LLMs) for document text translation. 
This app provides free translation capabilities using publicly available models and frameworks.
Application built on Windows. Some functionality and setup may need to be updated to deploy on other OS.

## 🌟 Features
* Text translation between English and multiple languages
* [Open-source Helisinki LLM integration](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models)
* User-friendly web-deployed interface
* Real-time translation
* No API keys or fees required
* Support for long text passages

## 🚀 Quick Start

### Prerequisites
* Python 3.8 or higher
* pip (Python package installer)
* A GitHub account
* A Streamlit Cloud account - free at [streamlit.io](https://streamlit.io/)

### Installation using bash

#### Step 1: Clone the repository in a new project folder
`mkdir translate-demo-app`
`cd translate-demo-app`
`git clone https://github.com/hnstaggs/translate-demo.git`

#### Step 2: Create a virtual environment
`python -m venv venv`
`cd venv`
`Scripts\activate`  # On Windows
  
#### Step 3: Install required packages
`cd ..`  # Back to root directory
`pip install -r requirements.txt`

#### Step 4: Run the app
`streamlit run app.py`

#### Step 5: App should automatically launch in browser. If not, Locate URL provided by streamlit console output and paste into web browser.
* Example: http://localhost:8501

#### Step 6: Deploying to Streamlit Cloud
* Push your code to your GitHub repository
* Log in to Streamlit Cloud
* Give Streamlit access to your github
* Click "New app"
* Select your repository, branch, and main file path (app.py)
* Click "Deploy"
* Your app will be live in the cloud at https://[translate-demo].streamlit.app

📦 Dependencies
* Windows 11
* Public facing github repo for project
* Up-to-date requirements.txt for streamlit deploy
* Packages: streamlit, transformers, torch, sentencepiece

💻 Usage
* Upload document needing translation
* Select target language from the dropdown menu
* Click "Translate"
* Download translated file

🛠️ Configuration: The app uses default settings, but you can modify config.yaml to:
* Change the default language pairs
* Adjust model parameters
* Customize the UI

⚠️ Limitations
* Translation quality may vary depending on the language pair
* Processing speed depends on your hardware capabilities
* Some language pairs might not be available in this build, but can be added based on model release

🙏 Acknowledgments/Credits
* Built with Streamlit Apache 2.0
* Uses Hugging Face Transformers Apache 2.0
* Inspired by open-source translation and deployment tools ⬇️

📚 Additional Resources, Citations, and Attributes
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Hugging Face Documentation](https://huggingface.co/docs/hub/index)
* [HelsinkiNLPModelCitation](https://github.com/Helsinki-NLP)
The Tatoeba Translation Challenge: Realistic Data Sets for Low Resource and Multilingual MT. Tiedemann, Jorg.
"Proceedings of the Fifth Conference on Machine Translation". Nov 2020. Online. Pages 1174-1182
"Association for Computational Linguistics". https://www.aclweb.org/anthology/2020.wmt-1.139

Made with ❤️ by Halee
