import streamlit as st
import pandas as pd


st.title("Data")
with st.expander("Curriculum Questions"):
    st.markdown(
        "Let's Read to Find Out (24 utterances)  \nExtension Questions (66 utterances)"
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

st.header("Curriculum Questions")

results_col1, results_col2 = st.columns(2)
results_col1.subheader("Let's Read to Find Out")
results_col1.markdown(
    "**Utterances:** 24  \n**Time:** 19 minutes  \n**Cost:** $2.47  \n**Overall Agreement:** 73.33%"
)

with results_col1.expander("**Results**"):
    lrtfo_df = pd.read_csv("data/LRTFO_agreement.csv")
    st.dataframe(lrtfo_df.set_index(lrtfo_df.columns[0]))

results_col2.subheader("Extension Questions")
results_col2.markdown(
    "**Utterances:** 66  \n**Time:** 54 minutes  \n**Cost:** $6.36  \n**Overall Agreement:** 87.08%"
)

with results_col2.expander("**Results**"):
    extention_qs_df = pd.read_csv("data/extension_qs_agreement.csv")
    st.dataframe(extention_qs_df.set_index(extention_qs_df.columns[0]))


st.divider()

st.header("TESOL SABR")

tesol_results_col1, tesol_results_col2 = st.columns(2)
tesol_results_col1.subheader("10% Random Sample")
tesol_results_col1.markdown(
    "**Utterances:** 160  \n**Time:** 2 hours  \n**Cost:** $14.34  \n**Overall Agreement:** x"
)

with tesol_results_col1.expander("**Results**"):
    tesol_10_df = pd.read_csv("data/tesol_10_gpt_agreement.csv")
    st.dataframe(tesol_10_df.set_index(tesol_10_df.columns[0]))

tesol_results_col2.subheader("20% Random Sample")
tesol_results_col2.markdown(
    "**Utterances:** 321  \n**Time:** x  \n**Cost:** x  \n**Overall Agreement:** 92.75%"
)

with tesol_results_col2.expander("**Results**"):
    st.caption("placeholder")
    # tesol_sabr_df = pd.read_csv("")
    # st.dataframe(tesol_sabr_df)

st.divider()

st.header("Official SABR")

st.markdown(
    "**Utterances:** 301  \n**Time:** x  \n**Cost:** x  \n**Overall Agreement:** x"
)


with st.expander("**Results**"):
    st.caption("placeholder")
    # tesol_sabr_df = pd.read_csv("")
    # st.dataframe(tesol_sabr_df)

st.divider()

st.subheader("Single Code - Only True")
code_ex_col1, code_ex_col2 = st.columns(2)

code_ex_col1.markdown("#")
code_ex_col1.markdown(
    "All utterances coded 1 for a specific code was collected from the SABR TESOL total then 20 utterances were randomly selected."
)
code_ex_col1.markdown("Each set was coded four times.")
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