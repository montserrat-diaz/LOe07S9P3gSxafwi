from sentence_transformers import util
import torch

def initial_cosine_similarities(query_embeddings, profile_embeddings):
  # Calculate cosine similarity for each query sentence separately
  similarities_query_1 = util.pytorch_cos_sim(torch.tensor(query_embeddings[0]), torch.tensor(profile_embeddings))
  similarities_query_2 = util.pytorch_cos_sim(torch.tensor(query_embeddings[1]), torch.tensor(profile_embeddings))

  # Combine the cosine similarities (e.g., taking the average)
  similarities_combined = (similarities_query_1 + similarities_query_2) / 2

  similarities_combined = similarities_combined.squeeze()
  return similarities_combined
