import streamlit as st

from docx import Document

import io

from translator import Translator

from utils import extract_text_from_docx, chunk_text, create_translated_document


def main():

    st.title("Document Translator")

    

    # Initialize translator

    translator = Translator()

    

    # File upload

    uploaded_file = st.file_uploader("Upload your English DOCX file", type=['docx'])

    

    # Language selection

    target_language = st.selectbox(

        "Select target language",

        options=list(translator.LANGUAGE_MODELS.keys())

    )

    

    if uploaded_file is not None:

        try:

            # Extract text from DOCX

            text_list = extract_text_from_docx(uploaded_file)

            

            # Show number of paragraphs found

            st.info(f"Found {len(text_list)} paragraphs in the document")

            

            if st.button("Translate"):

                with st.spinner("Loading translation model..."):

                    # Load the appropriate model

                    model_name = translator.LANGUAGE_MODELS[target_language]

                    model, tokenizer = translator.load_model(model_name)

                

                with st.spinner("Translating document..."):

                    # Split text into chunks

                    text_chunks = chunk_text(text_list)

                    

                    # Create a progress bar

                    progress_bar = st.progress(0)

                    

                    # Translate chunks

                    translated_chunks = []

                    for i, chunk in enumerate(text_chunks):

                        translated_chunk = translator.translate_text([chunk], model, tokenizer)

                        translated_chunks.extend(translated_chunk)

                        # Update progress bar

                        progress_bar.progress((i + 1) / len(text_chunks))

                    

                    # Create new document with translations

                    doc = create_translated_document(text_list, translated_chunks)

                    

                    # Save the document to bytes

                    doc_bytes = io.BytesIO()

                    doc.save(doc_bytes)

                    doc_bytes.seek(0)

                    

                    # Create download button

                    st.download_button(

                        label="Download translated document",

                        data=doc_bytes,

                        file_name=f"translated_{target_language}.docx",

                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"

                    )

                    

                    st.success("Translation completed!")

                    

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":

    main()