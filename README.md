# ScormVersion Converter

This project is designed to process SCORM packages by extracting files from ZIP archives, parsing XML files, and then re-zipping the files. The main script, `index.py`, handles the conversion of files within a specified directory.

## Background

We are transitioning from the ILIAS learning management system to SAP SuccessFactors. During this transition, we encountered an issue where SCORM packages in the 2004 3rd Edition format do not function correctly in SAP SuccessFactors, although they run without problems in ILIAS. This project aims to address this compatibility issue by converting the SCORM packages to a format that is compatible with SAP SuccessFactors.

## Project Structure

- `index.py`: The main script that orchestrates the conversion process.
- `ZIP.py`: Contains functions for extracting and zipping files.
- `ParseXML.py`: Contains functions for parsing XML files.

## Requirements

- Python 3.11 maybe it works with lower versions 
- Required Python packages: `os`, `ZIP`, `ParseXML`

## Usage

1. **Setup**: Ensure that the `ZIP.py` and `ParseXML.py` modules are in the same directory as `index.py`.

2. **Run the Script**: Execute the `index.py` script to start processing files in the specified directory.

3. **Files**: wich are in the folder data will be converted

```bash
python index.py
