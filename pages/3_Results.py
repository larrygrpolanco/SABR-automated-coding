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


st.subheader("Let's Read to Find Out (73.33%)")
st.markdown(
    "**Utterances:** 24  \n**Time:** 19 minutes  \n**Cost:** $2.47  \n**Overall Agreement:** 73.33%"
)

with st.expander("**Results**"):
    lrtfo_df = pd.read_csv("data/LRTFO_agreement.csv")
    st.dataframe(lrtfo_df.set_index(lrtfo_df.columns[0]))

st.subheader("Extension Questions (87.08%)")
st.markdown(
    "**Utterances:** 66  \n**Time:** 54 minutes  \n**Cost:** $6.36  \n**Overall Agreement:** 87.08%"
)

with st.expander("**Results**"):
    extention_qs_df = pd.read_csv("data/extension_qs_agreement.csv")
    st.dataframe(extention_qs_df.set_index(extention_qs_df.columns[0]))


st.divider()

st.header("TESOL SABR")

st.subheader("10% Random Sample (92.75%)")
st.markdown(
    "**Utterances:** 160  \n**Time:** 2 hours  \n**Cost:** $14.34  \n**Overall Agreement:** 92.75%"
)

with st.expander("**Results**"):
    tesol_10_df = pd.read_csv("data/tesol_10_gpt_agreement.csv")
    st.dataframe(tesol_10_df.set_index(tesol_10_df.columns[0]))


st.divider()

st.header("Official SABR")

st.subheader("20% Random Sample (94.83%)")
st.markdown(
    "**Utterances:** 60  \n**Time:** 43 minutes  \n**Cost:** $8.30  \n**Overall Agreement:** 94.83%"
)

with st.expander("**Results**"):
    official_sabr_df = pd.read_csv("data/offical_20_agreement.csv")
    st.dataframe(official_sabr_df.set_index(official_sabr_df.columns[0]))

st.divider()


st.header("Single Code - Only True")
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
    "Looking at only true cases makes it easier to see the AI's reasoning and what needs to be fixed."
)
code_ex_col1.caption("* Average cost: ~$0.05  \n* Average time: ~1-2 minutes")
code_ex_col1.caption("")

code_ex_col2.caption("Human Code Sample:")

code_ex_col2.image("Assets/cog_raw_code_example.png")


with st.expander("Sequence/Temporal **(45.83%)**"):
    code_ex_col1, cod_ex_col2 = st.columns(2)

    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 45.83% ")
    st.markdown("* Intra-rater: 86.11%")
    st.caption("\* only 12 codes")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/seq_12_gpt_1.csv")
    st.dataframe(df_seq)

with st.expander("Compare & Contrast **(81.25%)**"):
    code_ex_col1, cod_ex_col2 = st.columns(2)
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 81.25% ")
    st.markdown("* Intra-rater: 89.17%")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/comp_20_gpt_1.csv")
    st.dataframe(df_seq)

with st.expander("Cognition **(78.75%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 78.75% ")
    st.markdown("* Intra-rater: 97.5%")
    st.caption("ChatGPT coding example:")
    df_cog = pd.read_csv("data/cog_20_gpt_1.csv")
    st.dataframe(df_cog)

with st.expander("Desires Preferences **(83.75%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 83.75% ")
    st.markdown("* Intra-rater: 84.50%")
    st.caption("ChatGPT coding example:")
    df_desire = pd.read_csv("data/desire_20_gpt_1.csv")
    st.dataframe(df_desire)

with st.expander("Feelings Emotions **(83.75%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 83.75% ")
    st.markdown("* Intra-rater: 92.50%")
    st.caption("ChatGPT coding example:")
    df_feelings = pd.read_csv("data/feelings_20_gpt_1.csv")
    st.dataframe(df_feelings)

with st.expander("Judgment & Perspective **(48.75%)**"):
    code_ex_col1, cod_ex_col2 = st.columns(2)
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 48.75%")
    st.markdown("* Intra-rater: 80.83%")
    st.caption("ChatGPT coding example:")
    df_seq = pd.read_csv("data/judg_20_gpt_1.csv")
    st.dataframe(df_seq)

with st.expander("Causal Effects Problem Solve **(90%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 90% ")
    st.markdown("* Intra-rater: 90%")
    st.caption("ChatGPT coding example:")
    df_causal = pd.read_csv("data/causal_20_gpt_1.csv")
    st.dataframe(df_causal)

with st.expander("Predictions Forecast **(36.25%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 36.25% ")
    st.markdown("* Intra-rater: 92.50%")
    st.caption("ChatGPT coding example:")
    df_predict = pd.read_csv("data/predict_20_gpt_1.csv")
    st.dataframe(df_predict)

with st.expander("Making Connections **(26.25%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 26.25% ")
    st.markdown("* Intra-rater: 89.17%")
    st.caption("ChatGPT coding example:")
    df_connect = pd.read_csv("data/connect_20_gpt_1.csv")
    st.dataframe(df_connect)

with st.expander("Background Knowledge **(27.50%)**"):
    st.markdown("**Average Agreement**")
    st.markdown("* Inter-rater: 27.50% ")
    st.markdown("* Intra-rater: 86.67%")
    st.caption("ChatGPT coding example:")
    df_back = pd.read_csv("data/back_20_gpt_1.csv")
    st.dataframe(df_back)

st.divider()
