# Repository for Fall 2022 Quarter (DSC180a)

## Explanation of File Structure:

### 📁 Folders:

#### data
Contains the data for and from the project, divided as such:
- raw: the base uncleaned data
- out: the output cleaned data used for visualizations and modeling
- test: test data used to debug the Python scripts
- visuals: visuals generated from the EDA and modeling, formatted as PNGs

#### notebooks
Contains initial Jupyter Notebooks for EDA / Modeling.
Not entirely cleaned up yet. Cleaned versions of this code will be found inside our `src` folder.

#### src
Contains the Python scripts needed to run the project, divided as such:
- data: `make_dataset.py` cleans and processes the raw data
- models: `relevance.py` trains the relevance classifier and generates plots of the resulting model & `score.py` does the same for the scoring model. 
- viz: `visualization.py` generates preliminary EDA visuals
- unused: `app.py` is a now-deprecated Streamlit app used for demoing EDA early into Quarter 1

### 📜 Files:

#### run.py
Baseline Python script to run via CLI with targets.
Current targets include `test` and `data`. 

### requirements.txt
Necessary Python packages to install via `pip install -r requirements.txt`
