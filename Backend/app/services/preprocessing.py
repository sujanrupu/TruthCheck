import re
import logging
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode

# Setup logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("preprocessing.log"), logging.StreamHandler()]
)
logger = logging.getLogger("TextPreprocessor")

# Load NLP model
nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def remove_special_characters(text):
    """Remove special characters, symbols, and punctuation from text."""
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

def normalize_unicode(text):
    """Normalize Unicode characters to ASCII."""
    return unidecode(text)

def tokenize_text(text):
    """Tokenize text using NLTK's word_tokenize."""
    return word_tokenize(text)

def remove_stopwords(tokens):
    """Remove stopwords from tokenized text."""
    return [word for word in tokens if word.lower() not in stop_words]

def lemmatize_text(tokens):
    """Perform lemmatization using spaCy NLP model."""
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]

def preprocess_text(text):
    """
    Complete text preprocessing pipeline including:
    - Unicode normalization
    - Lowercasing
    - Special character removal
    - Tokenization
    - Stopword removal
    - Lemmatization
    """
    try:
        if not text or not isinstance(text, str):
            raise ValueError("Invalid text input: Must be a non-empty string.")
        
        logger.info(f"Original Text: {text}")
        
        text = normalize_unicode(text.lower())
        text = remove_special_characters(text)
        tokens = tokenize_text(text)
        tokens = remove_stopwords(tokens)
        tokens = lemmatize_text(tokens)
        
        preprocessed_text = " ".join(tokens)
        logger.info(f"Preprocessed Text: {preprocessed_text}")
        
        return preprocessed_text
    except Exception as e:
        logger.error(f"Error in text preprocessing: {str(e)}")
        return ""

# Example Usage
def main():
    sample_texts = [
        "COVID-19 vaccines are effective and safe!",
        "The Eiffel Tower, a global landmark, is in Paris.",
        "Elon Musk founded Tesla, SpaceX, and Neuralink.",
        "Water boils at 100 degrees Celsius under normal conditions.",
        "Unicorns are mythical creatures found in folklore."
    ]
    
    for text in sample_texts:
        processed = preprocess_text(text)
        print(f"Processed: {processed}\n")

if __name__ == "__main__":
    main()
