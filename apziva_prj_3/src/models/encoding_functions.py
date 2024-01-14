from sentence_transformers import SentenceTransformer

# Function for encoding data and initial query
def encoding_data_and_query(model_name, query_sentences):
  model = SentenceTransformer(model_name)

  # Encoding profiles
  profile_embeddings = model.encode(data_concat['data_concat'])

  # Encoding query sentences
  query_embeddings = model.encode(query_sentences)

  return model, profile_embeddings, query_embeddings

# Function for encoding new query
def encoding_new_query(model, selected_profile):
  new_query_sentence = [selected_profile]
  new_query_embedding = model.encode(new_query_sentence)
  return new_query_embedding
