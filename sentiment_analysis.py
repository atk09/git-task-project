# Import necessary libraries
import pandas as pd
import spacy
import spacytextblob
import warnings

# Disable spaCy warning
warnings.filterwarnings("ignore", message=r".*\[W007\].*", category=UserWarning)

# Load the spaCy model for English language
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def preprocess_text(text):
    """Preprocess the text data by tokenizing, removing stopwords, and punctuation."""
    doc = nlp(text)
    processed_text = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return doc, processed_text

def analyze_sentiment(doc):
    """Analyze sentiment score and determine polarity."""
    sentiment_score = doc._.polarity
    polarity = 'positive' if sentiment_score > 0 else 'negative' if sentiment_score < 0 else 'neutral'
    return polarity

def test_similarity(review1, review2):
    """Test the similarity between two tokenized reviews."""
    similarity_score = review1.similarity(review2)
    return similarity_score

def main():
    # Read CSV file with correct column names and data types
    reviews_data = pd.read_csv('amazon_product_reviews.csv', dtype={1: str, 10: str})
    
    # Drop missing values
    reviews_text = reviews_data['reviews.text'].dropna()
    
    # Select two random reviews
    review1_text = reviews_text.sample(n=1).iloc[0]
    review2_text = reviews_text.sample(n=1).iloc[0]
    
    # Preprocess the selected reviews
    review1_doc, preprocessed_review1 = preprocess_text(review1_text)
    review2_doc, preprocessed_review2 = preprocess_text(review2_text)
    
    # Analyze sentiment and determine polarity for each review
    polarity_review1 = analyze_sentiment(review1_doc)
    polarity_review2 = analyze_sentiment(review2_doc)
    
    # Determine the similarity between the selected reviews
    similarity_score = test_similarity(review1_doc, review2_doc)
    
    # Print the results
    print("Selected reviews for analysis:")
    print("Review 1:", review1_text)
    print("Review 2:", review2_text)
    print("Polarity of Review 1:", polarity_review1)
    print("Polarity of Review 2:", polarity_review2)
    print("Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()
