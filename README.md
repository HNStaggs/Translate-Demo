![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# LLM Translation App
A streamlit-based application that leverages open-source, pretrained Large Language Models (LLMs) for document text translation. 
This app provides free translation capabilities using publicly available models and frameworks.
Application built on Windows. Some functionality and setup may need to be updated to deploy on other OS.

## 🌟 Features
* Text translation between English and multiple languages - arabic, chinese, french, german, hindi, italian, japanese, portuguese, russian, spanish 
* [Open-source Helisinki-NLP OPUS models](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models)
* User-friendly web-deployed interface
* Real-time translation
* No API keys or fees required
* No GPU needed

### Minimum/Recommended Requirements:
- RAM: 4GB/8GB
- Storage: 2GB/5GB free space
- CPU: Any modern processor/multi-score processor (2 cores+/4 cores+)

## 🚀 Quick Start

### Prerequisites
* Python 3.9+
* pip (Python package installer)
* A GitHub account
* A Streamlit Cloud account - free at [streamlit.io](https://streamlit.io/)

### Installation using bash

#### Step 1: Clone the repository in a new project folder
1. `mkdir translate-demo-app`
2. `cd translate-demo-app`
3. `git clone https://github.com/hnstaggs/translate-demo.git`

#### Step 2: Create a virtual environment
4. `python -m venv venv`
5. `cd venv`
6. `Scripts\activate`  # On Windows
  
#### Step 3: Install required packages
7. `cd ..`  # Back to root directory
8. `pip install -r requirements.txt`

#### Step 4: Run the app
9. `streamlit run src/app.py`

#### Step 5: App should automatically launch in your browser
* If not, Locate URL provided by streamlit console output and paste into web browser.
* Example: http://localhost:8501
* Test app functionality on your machine

#### Step 6: Deploying to Streamlit Cloud to Share with Others
* Push your code to your GitHub repository
* Log in to Streamlit Cloud
* Give Streamlit access to your github
* Click "New app"
* Select your repository, branch, and main file path (app.py)
* Click "Deploy"
* Your app will be live in the cloud at https://[translate-demo].streamlit.app

## 📦 Dependencies
* Windows
* Public facing github repo for project
* Up-to-date requirements.txt for streamlit deploy
* Streamlit
* Transformers
* PyTorch
* python-docx
* Git

## 💻 Usage
* Upload document needing translation
* Select target language from the dropdown menu
* Click "Translate"
* Download translated file

## 🛠️  Package Configuration
* The setup.py file configures the project as a Python package with:
- Project name and version
- Dependencies
- Author information
- Project description
- Python version requirements

* You can modify setup.py to:
- Add new dependencies
- Update project metadata
- Configure entry points
- Set minimum Python version

## ⚠️ Limitations
* Translation quality may vary depending on the language pair
* Processing speed depends on your hardware capabilities
* Some language pairs might not be available in this build, but can be added based on model release
* Max docX size 5-7 pages
* Formatting may not be preserved

## 🙏 Acknowledgments/Credits
* Built with Streamlit Apache 2.0
* Uses Hugging Face Transformers Apache 2.0
* Inspired by open-source translation and deployment tools ⬇️

## 📚 Additional Resources, Citations, and Attributes
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Hugging Face Documentation](https://huggingface.co/docs/hub/index)
* [HelsinkiNLPModelCitation](https://github.com/Helsinki-NLP)
The Tatoeba Translation Challenge: Realistic Data Sets for Low Resource and Multilingual MT. Tiedemann, Jorg.
"Proceedings of the Fifth Conference on Machine Translation". Nov 2020. Online. Pages 1174-1182
"Association for Computational Linguistics". https://www.aclweb.org/anthology/2020.wmt-1.139
* [OPUS](https://opus.nlpl.eu/)
- opus-mt-en-ar (Arabic)
- opus-mt-en-zh (Chinese)
- opus-mt-en-fr (French)
- opus-mt-en-de (German)
- opus-mt-en-hi (Hindi)
- opus-mt-en-it (Italian)
- opus-mt-en-jap (Japanese)
- opus-mt-en-pt (Portuguese)
- opus-mt-en-ru (Russian)
- opus-mt-en-es (Spanish)

# Made with ❤️ by Halee

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
