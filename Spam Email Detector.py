# Simple Rule-Based Spam Email Detector

def check_spam(email_text):
    # Common spam trigger words
    spam_words = ["free", "winner", "congratulations", "cash", "prize", "urgent", "claim"]
    
    text_lower = email_text.lower()
    detected_keywords = [word for word in spam_words if word in text_lower]
    
    # Classification logic
    if len(detected_keywords) >= 2:
        return "SPAM EMAIL DETECTED", detected_keywords
    elif len(detected_keywords) == 1:
        return "SUSPICIOUS EMAIL", detected_keywords
    else:
        return "CLEAN / LEGITIMATE EMAIL", []

# Main Execution
print("=== AI/NLP Rule-Based Spam Email Filter ===")
user_email = input("Paste email body text here: ")

result, matches = check_spam(user_email)

print(f"\nResult: {result}")
if matches:
    print(f"Flagged Keywords: {', '.join(matches)}")