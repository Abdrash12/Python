from textblob import TextBlob
from nltk.corpus import stopwords
from collections import Counter
import string
import nltk

# Make sure these are downloaded (run once)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

def preprocess_review(review):
    """Removes stopwords, punctuation, and converts to lowercase."""
    stop_words = set(stopwords.words('english'))
    # Lowercase
    review = review.lower()
    # Remove punctuation
    review = review.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    words = nltk.word_tokenize(review)
    # Remove stopwords
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

def analyze_sentiment(preprocessed_review):
    """Calculates polarity and subjectivity using TextBlob."""
    blob = TextBlob(preprocessed_review)
    polarity = blob.sentiment.polarity  # -1 (negative) to 1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)
    return polarity, subjectivity

def extract_keywords(preprocessed_review):
    """Identifies the most frequent nouns and adjectives."""
    blob = TextBlob(preprocessed_review)
    # Get word-tag pairs (POS tagging)
    tagged_words = blob.tags
    # Extract nouns and adjectives
    keywords = [word for word, tag in tagged_words if tag.startswith('NN') or tag.startswith('JJ')]
    # Count frequency
    most_common = Counter(keywords).most_common(5)
    return [word for word, _ in most_common]

def categorize_review(polarity, subjectivity, keywords):
    """Classifies reviews based on polarity, subjectivity, and keywords."""
    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    if subjectivity > 0.5:
        tone = "Opinionated"
    else:
        tone = "Factual"
    
    return f"{sentiment} | {tone} | Keywords: {', '.join(keywords)}"

# Example usage
review_text = "The movie was absolutely amazing with stunning visuals, but a bit too long."
clean_review = preprocess_review(review_text)
pol, subj = analyze_sentiment(clean_review)
key_words = extract_keywords(clean_review)
category = categorize_review(pol, subj, key_words)

print("Preprocessed Review:", clean_review)
print("Polarity:", pol, "Subjectivity:", subj)
print("Keywords:", key_words)
print("Category:", category)
