import streamlit as st
import pandas as pd
import numpy as np
from itertools import combinations


# Load dataframe function remains unchanged
def load_dataframe(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    else:
        return pd.DataFrame()  # Return an empty DataFrame if file type is unknown


def calculate_percent_agreement(dfs, columns_to_compare):
    agreement_scores = []
    for df1, df2 in combinations(
        dfs, 2
    ):  # Iterate over every combination of file pairs
        pair_scores = []
        for col in columns_to_compare:
            # Normalize data types for comparison; here converting everything to strings for simplicity
            col1 = df1[col].astype(str).str.lower()  # Convert to string and lowercase
            col2 = df2[col].astype(str).str.lower()  # Convert to string and lowercase

            non_null_mask = (
                ~col1.isnull() & ~col2.isnull()
            )  # Ensure non-null values in both
            if non_null_mask.sum() > 0:  # If there are non-null values to compare
                agreement = np.mean(
                    col1[non_null_mask] == col2[non_null_mask]
                )  # Calculate mean agreement
                pair_scores.append(agreement)
        if pair_scores:
            agreement_scores.append(np.mean(pair_scores))
    return np.mean(agreement_scores) if agreement_scores else None


st.title("Intra-Rater Reliability Checker")
st.markdown(
    "Program takes in tables and checks agreement for every combination in pairs then gives the mean agreement."
)

# File uploaders in an expander
with st.expander("Load Files"):
    uploaded_files = st.file_uploader(
        "Choose CSV or Excel files", accept_multiple_files=True, type=["csv", "xlsx"]
    )
    dataframes = [load_dataframe(file) for file in uploaded_files if file is not None]
    if len(dataframes) >= 2:  # Ensure at least two files are loaded
        st.success("Files successfully loaded.")

if len(dataframes) >= 2:
    common_columns = list(set.intersection(*(set(df.columns) for df in dataframes)))

    columns_to_compare = st.multiselect(
        "Choose columns",
        options=common_columns,
    )

    if st.button("Calculate Intra-Rater Reliability"):
        percent_agreement = calculate_percent_agreement(dataframes, columns_to_compare)
        if percent_agreement is not None:
            st.metric(label="Percent Agreement", value=f"{percent_agreement:.2%}")
        else:
            st.error(
                "Could not calculate percent agreement. Ensure there are common columns with data to compare."
            )

    for i, df in enumerate(dataframes, start=1):
        if st.button(f"Show File {i}"):
            st.dataframe(df)
