import PyPDF2
import matplotlib.pyplot as plt
from collections import Counter

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to create a bar chart of word frequencies
def create_bar_chart(text, num_top_words=10):
    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Select the most common words
    top_words = word_counts.most_common(num_top_words)

    # Extract words and frequencies for plotting
    words = [word[0] for word in top_words]
    frequencies = [word[1] for word in top_words]

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='orange')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {num_top_words} Most Common Words')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Path to your PDF file
pdf_path = "docs/5vdcsupply.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Create bar chart of word frequencies
create_bar_chart(pdf_text, num_top_words=10)  # You can adjust num_top_words as needed
