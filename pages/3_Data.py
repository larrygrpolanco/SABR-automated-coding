import streamlit as st
import pandas as pd


st.title("Data")
with st.expander("Extension Questions"):
    st.markdown(
        "Let's Read to Find Out (69 utterances)  \nExtension Questions (86 utterances)"
    )
    st.caption("All codes removed but meaning codes e.g.,")
    st.image("Assets/extension_qs.png")

with st.expander("TESOL SABR Codes"):
    st.markdown(
        "16 transcripts (key sections combined)  \n2 Coders  \n1603 utterances  \nStripped down to meaning codes similar to extension questions"
    )

with st.expander("SABR Offical Practice Transcript"):
    st.markdown("Coded transctipt by SABR developers (302 utterances)")
    st.caption(
        "While they had their own reliability checker I was only doing meaning codes and it seemed to cause some issues with excel formulas e.g.,"
    )
    st.image("Assets/official_sabr_gpt_test.png")

st.divider()

st.title("Methods/Results")
st.markdown(
    "There were many iterations of this program, but I will just go through the most recent. I have not tried to improve the mothods or results. I am not sure how best to continue."
)

with st.expander("Chain-of-Though Prompting"):
    st.markdown(
        "Prompting scheme modeled after a paper on chain of thought prompting -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning"
    )
    st.code(
        """
    Use the following format: 
    Step 1:{delimiter} <Your decision-making process analysis. Summarize how the coding manual lead you to conclude whether the utterance meets the criteria for the code.> 
    Step 2:{delimiter}<Your final code decision. Only include '1' if the utterance meets the criteria, or 'X' if it does not. No additional text should be here.> 
            """
    )
    st.markdown("Can definetly be imporved with testing.")
    st.caption(
        "Reference  \nWei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35, 24824-24837. https://doi.org/10.48550/arXiv.2201.11903 "
    )

st.divider()
st.subheader("Single Code - Only True")
code_ex_col1, code_ex_col2 = st.columns(2)

code_ex_col1.markdown("#")
code_ex_col1.markdown(
    "All utterances coded 1 for a specific code was collected from the SABR TESOL total then 20 utterances were randomly selected."
)
code_ex_col1.markdown("* Each set was coded four times.")
code_ex_col1.markdown(
    "Intra-rater reliability is the mean agreement across every pair combination."
)
code_ex_col1.caption(
    "Note: Looking at only true cases makes it easier to see the AI's reasoning and what needs to be fixed."
)
code_ex_col1.caption("* Average cost: ~$0.05  \n* Average time: ~1-2 minutes")
code_ex_col1.caption("")

code_ex_col2.caption("Human Code Sample:")

code_ex_col2.image("Assets/cog_raw_code_example.png")


with st.expander("Cognition (78.75%)"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 78.75% ")
    st.markdown("* Intra-rater: 97.5%")
    st.caption("ChatGPT coding example:")
    df_cog = pd.read_csv("data/cog_20_gpt_1.csv")
    st.dataframe(df_cog)

with st.expander("Sequence/Temporal (45.83%)"):
    code_ex_col1, cod_ex_col2 = st.columns(2)
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 80% ")
    st.markdown("* Intra-rater: 86.11%")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/seq_12_gpt_1.csv")
    st.dataframe(df_seq)

with st.expander("Compare & Contrast (81.25%)"):
    code_ex_col1, cod_ex_col2 = st.columns(2)
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 81.25% ")
    st.markdown("* Intra-rater: 89.17%")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/comp_20_gpt_1.csv")
    st.dataframe(df_seq)

with st.expander("Judgment & Perspective (48.75%)"):
    code_ex_col1, cod_ex_col2 = st.columns(2)
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 48.75%")
    st.markdown("* Intra-rater: 80.83%")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/judg_20_gpt_1.csv")
    st.dataframe(df_seq)

st.divider()

st.subheader("TESOL SABR Tests")
st.caption("Sequence/Temporal, Compare/Contrast, Cognition, Desires/Preferences"
        "Feelings/Emotions",
        "Judgments/Perspectives",
        "Causal Effects & Problem Solving",
        "Predictions/Forecast",
        "Making Connections",
        "Building Knowledge"
tesol_col1, tesol_col2 = st.columns(2)
tesol_col1.subheader("10% Random Sample")
tesol_col1.markdown("**Utterances:** 160  \n**Time:** x  \n**Cost:** x  ")

tesol_col2.subheader("20% Random Sample")
tesol_col2.markdown("**Utterances:** 321  \n**Time:** x  \n**Cost:** x  ")

with st.expander("**Results**"):
    st.caption("placeholder")
    # tesol_sabr_df = pd.read_csv("")
    # st.dataframe(tesol_sabr_df)
