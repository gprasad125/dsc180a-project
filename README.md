# Repository for Fall 2022 Quarter (DSC180a)

## Explanation of File Structure:

### Folders:

#### data
Contains initial dataset (CSVs) containing Tweet information
Fields include: Tweet text, Tweet account, Account's role in Congress, Sentiment score, etc.
Raw, uncleaned data found in `raw` while cleaned data for visualization & modeling is in `out`.

#### notebooks
Contains initial Jupyter Notebooks for EDA / Modeling.
Not entirely cleaned up yet. Cleaned versions of this code will be found inside our `src` folder.

#### src
Contains the Python scripts needed to run the project, divided as such:
- `make_dataset.py`: Cleans data found in `data/raw` and outputs the final versions to `data/out`
- `app.py`: Outdated version of a Streamlit app used for presentation in Week 2. No longer used.
- ``
