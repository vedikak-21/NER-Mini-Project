import streamlit as st
import spacy
import pandas as pd
from io import StringIO

# Configure the application
st.set_page_config(
    page_title="NER System",
    page_icon="🔍",
    layout="wide"
)

# Load the pretrained NLP model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

try:
    nlp = load_model()
except OSError:
    st.error(
        "The spaCy English model is missing. "
        "Run: python -m spacy download en_core_web_sm"
    )
    st.stop()


# Application title
st.title("🔍 Named Entity Recognition System")
st.write(
    "An NLP application that identifies and classifies "
    "named entities in text."
)

st.info(
    "Supported entity types include people, organizations, "
    "locations, dates, money, and more."
)


# Text input
st.subheader("1. Enter Your Text")

sample_text = (
    "Sundar Pichai is the CEO of Google. "
    "He visited Mumbai on 15 October 2026 and announced "
    "an investment of 500 million dollars."
)

text_input = st.text_area(
    "Enter text to analyze:",
    value=sample_text,
    height=150,
    placeholder="Paste your text here..."
)

# File upload
uploaded_file = st.file_uploader(
    "Or upload a text file (.txt)",
    type=["txt"]
)

if uploaded_file is not None:
    try:
        file_text = uploaded_file.getvalue().decode("utf-8-sig")
        text_input = file_text
        st.success("Text file uploaded successfully!")
    except UnicodeDecodeError:
        st.error("Could not read the file. Please upload a UTF-8 text file.")
        text_input = ""


# Analyze text
if st.button("🔎 Extract Named Entities", type="primary"):

    if not text_input.strip():
        st.warning("Please enter some text or upload a text file.")

    else:
        doc = nlp(text_input)

        entities = [
            {
                "Entity": ent.text,
                "Entity Type": ent.label_,
                "Start Position": ent.start_char,
                "End Position": ent.end_char
            }
            for ent in doc.ents
        ]

        st.subheader("2. Highlighted Text")

        if entities:
            colors = {
                "PERSON": "#FFD6D6",
                "ORG": "#D6E8FF",
                "GPE": "#D6F5D6",
                "LOC": "#E8D6FF",
                "DATE": "#FFF0B3",
                "TIME": "#FFE0B3",
                "MONEY": "#B3F0E8",
                "PRODUCT": "#F5D6FF",
                "EVENT": "#FFD9B3",
                "NORP": "#D6F0F0",
                "FAC": "#E0E0E0",
                "WORK_OF_ART": "#F5E6CC",
                "LAW": "#DCE6F1",
                "PERCENT": "#FADBD8",
                "QUANTITY": "#D5F5E3",
                "ORDINAL": "#E8DAEF",
                "CARDINAL": "#FCF3CF"
            }

            highlighted_html = spacy.displacy.render(
                doc,
                style="ent",
                options={"colors": colors}
            )

            st.html(highlighted_html)

        else:
            st.info("No named entities were detected.")

        st.subheader("3. Extracted Entities")

        if entities:
            df = pd.DataFrame(entities)

            # Display entity counts
            total_entities = len(df)
            unique_entities = df["Entity"].nunique()

            col1, col2 = st.columns(2)

            col1.metric("Total Entities", total_entities)
            col2.metric("Unique Entity Texts", unique_entities)

            st.dataframe(df, use_container_width=True)

            # Entity type distribution
            st.subheader("4. Entity Type Distribution")

            counts = df["Entity Type"].value_counts()
            st.bar_chart(counts)

            # Download results
            csv_data = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇️ Download Results as CSV",
                data=csv_data,
                file_name="ner_results.csv",
                mime="text/csv"
            )

            # Explanation of entity types
            st.subheader("5. Entity Type Guide")

            descriptions = {
                "PERSON": "People's names",
                "ORG": "Companies and organizations",
                "GPE": "Countries, cities, and geopolitical entities",
                "LOC": "Geographical locations",
                "DATE": "Dates and periods",
                "TIME": "Times of day",
                "MONEY": "Monetary values",
                "PRODUCT": "Products",
                "EVENT": "Named events",
                "NORP": "Nationalities, religious or political groups",
                "FAC": "Buildings, airports, roads, and facilities",
                "WORK_OF_ART": "Titles of creative works",
                "LAW": "Named laws",
                "PERCENT": "Percentages",
                "QUANTITY": "Measurements and quantities",
                "ORDINAL": "First, second, third, etc.",
                "CARDINAL": "Numerical values that do not fit other categories"
            }

            guide_df = pd.DataFrame([
                {
                    "Entity Type": label,
                    "Meaning": descriptions.get(label, "Named entity category")
                }
                for label in sorted(df["Entity Type"].unique())
            ])

            st.dataframe(guide_df, use_container_width=True)

        else:
            st.write("There are no entities to display.")

