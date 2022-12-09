## Setup
download and install
corpora/omw-1.4
coprora/wordnet
tokenizers/punkt

- download them manually or using nltk.download()
- auto download does not work under venv (poetry)

Manual installation
- mkdir ~/nltk_data
- from https://www.nltk.org/nltk_data/ download necessary corpora
- copy them to the created folder and put under specified subfolders (see above)
- unzip and renamed in a specific way (see above)

- install poetry
- run `$poetry install` to install necessary dependencies

## Run
`poetry run python process_words/process.py ./sample.txt`