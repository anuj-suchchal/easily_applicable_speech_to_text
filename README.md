Easily Applicable Speech-to-Text engine (EAST engine)
Welcome to Easily Applicable Speech-to-Text Engine. With the help of this engine you can easily transcribe speech to text in different languages using different models. Below are the steps how to transcribe an audio file stored in a local folder. These steps are meant for Linux OS.
1. Create a separate python environment using below command:-
python -m venv env_files_east
2. Activate the environment:-
source env_files_east/bin/activate
3. Run requirements.txt to install required packages.
pip install -r requirements.txt
4. Setup is done. Now you can run transcribe file with different options-
python transcribe.py
