# Merriam-Webster Dictionary CLI

This is a simple command line tool that allows users to query the Merriam-Webster dictionary and receive a formatted response with the word definition, synonyms, and antonyms.

Will Upload the PDF of the task after seeking gracious permission


## Requirements

- Python 3.x
- pip

## Installation

1. Clone this repository:
git clone https://github.com/Anuj359/Avalara.git

2. Install the required packages:

## Usage

To use the tool, simply run the following command:
make run <word> or
python3 task.py <word>

Replace `<word>` with the word you want to look up. For example, to look up the word "exercise", run:
make run exercise

Or

You can only use the github action "definition" and trigger the action by passing your requested <word>


## Testing
Haven't written any tests yet.

## Directory Structure

- `task.py`: The main Python script that contains the implementation of the command line tool.
- `Makefile`: The build pipeline for the tool.
- `README.md`: This file.
- `.github/workflows/definition.yaml`: The Github action to manually trigger the code and get definition

## License
I only own my driving license that's it, this repo is all yours xD :p