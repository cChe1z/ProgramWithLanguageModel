from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine the sentiment category
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    # Take text input from the user
    text = input("Enter a text string to analyze: ")
    
    # Analyze sentiment
    sentiment = analyze_sentiment(text)
    
    # Output the sentiment
    print(f"The sentiment of the text is: {sentiment}")

if __name__ == "__main__":
    main()




