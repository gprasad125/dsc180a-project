# Repository for Fall 2022 Quarter (DSC180a)

This project covers Tweet sentiment analysis for Tweets originating from US congresspeople as it relates to China.

## Data Source:

Raw data can be found [here](https://drive.google.com/drive/u/1/folders/1VSYdGh12UNVNhfxbSeHRdANvHr5xF8Ea). 
Download the file `SentimentLabeled_10112022.csv`, and place it inside the `data/raw` directory. 

You can then run the `run.py` file with the following targets:
- `test`: runs the file on man-made test data
- `data`: runs the file on Twitter-API sourced data.

## Explanation of File Structure:

### 📁 Folders:

#### config
Contains JSON configuration for optimized & group-selected models. 

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
- models: 
    - Vanilla Models: 
        - `relevance.py` trains the relevance classifier and generates plots of the resulting model 
        - `score.py` does the same for the scoring model.
    - Optimized Models:
        - `opt_model_relevancy.py` trains the relevance classifier with optimized parameters
        - `best_classifier` uses the group's best decided classifier
        - `best_scoring` uses the group's best decided scoring model
        [^1]: There is no optimized file for the scoring model as the best parameters were default
- viz: `visualization.py` generates preliminary EDA visuals
- unused: `app.py` is a now-deprecated Streamlit app used for demoing EDA early into Quarter 1

### 📜 Files:

#### run.py
Baseline Python script to run via CLI with targets.
Current targets include `test` and `data`. 

    - Creates cleaned data file
    - Generates exploratory visuals and saves them
    - Runs vanilla, optimized, and group-selected models on data, and saves them in txt file

### requirements.txt
Necessary Python packages to install via `pip install -r requirements.txt`
