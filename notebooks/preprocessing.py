import os, sys
import numpy as np
import pandas as pd
import spacy

import string
import re

def preprocess_spacy(
    text,
    min_token_len=2,
    irrelevant_pos=["ADV", "PRON", "CCONJ", "PUNCT", "NUM", "SYM"],
):
    """
    Given text, min_token_len, and irrelevant_pos carry out preprocessing of the text
    and return a preprocessed string.

    Parameters
    -------------
    text : (spaCy doc object)
        the spacy doc object of the text
    min_token_len : (int)
        min_token_length required
    irrelevant_pos : (list)
        a list of irrelevant pos tags

    Returns
    -------------
    (str) the preprocessed text
    """
    
    clean_text = []
    
    for token in text:
        if (
            token.is_stop == False # Check if it's not a stopword
            and len(token) > min_token_len  # Check if the word meets minimum threshold
            and token.pos_ not in irrelevant_pos # Check if the POS is in the acceptable POS tags
        ):  
            lemma = token.lemma_  
            clean_text.append(lemma.lower()) 
            
    return " ".join(clean_text)

import re
def preprocess(text):
    # Replace a sequence of whitespaces by a single whitespace
    text = re.sub(r"\s+", " ", text)
    
    # Remove other strange characters
    text = re.sub(r"""[\n\r]+""", "", text)
    
    # Remove other strange characters
    text = re.sub(r"""[\*\~\;]+""", "", text)

    # Replace slashes with spaces
    text = re.sub(r"""[\/]+""", " ", text)

    return text