from sentence_transformers import SentenceTransformer
def encoding_data_and_query(model_name, query_sentences):
  model = SentenceTransformer(model_name)

  # Encoding profiles
  profile_embeddings = model.encode(data_concat['data_concat'])

  # Encoding query sentences
  query_embeddings = model.encode(query_sentences)

  return model, profile_embeddings, query_embeddings
