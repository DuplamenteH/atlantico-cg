# Import necessary modules
from nltk.tokenize import word_tokenize , sent_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

# Split scene_one into sentences: sentences
scene_one = get_sample_Santo_Graal()
sentences = scene_one[3]

# Use word_tokenize to tokenize the fourth sentence: tokenized_sent
tokenized_sent = word_tokenize(sentences[3])

# Make a set of unique tokens in the entire scene: unique_tokens
unique_tokens = set(word_tokenize(scene_one))

# Print the unique tokens result
print(unique_tokens)