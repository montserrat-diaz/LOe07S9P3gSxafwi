import sys

REQUIRED_PYTHON = "python3"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")

    # Load data
    file_path = "potential-talents - Aspiring human resources - seeking human resources.csv"
    data = load_data(file_path)
    
    # Preprocess data
    data_concat = preprocess_data(data)
    
    # Encode data and query with SBERT model
    model, profile_embeddings_sbert, query_embeddings_sbert = encoding_data_and_query('paraphrase-distilroberta-base-v1', ['aspiring human resources', 'seeking human resources'])
    
    # Calculate cosine similarities 
    similarities_combined = initial_cosine_similarities(query_embeddings_sbert, profile_embeddings_sbert)
    
    # Assign the combined similarities to the DataFrame
    data_concat['cosine_similarity_sbert'] = similarities_combined.cpu().numpy().tolist()
    
    # Rank and display profiles based on cosine similarity scores
    ranked_profiles = rank_and_display_profiles(data_concat, 'cosine_similarity_sbert')
    
    # Select and display a profile
    selected_profile = select_and_display_profile(data_concat)
    
    # Encode query sentence for the selected profile
    new_query_embedding = encoding_new_query(model, selected_profile)
    
    # Calculate cosine similarity for the new query sentence
    similarities = util.pytorch_cos_sim(torch.tensor(new_query_embedding[0]), torch.tensor(profile_embeddings_sbert))
    
    similarities = similarities.squeeze()
    
    # Assign the new similarities to the DataFrame
    data_concat['cosine_similarity_sbert'] = similarities.cpu().numpy().tolist()
    
    # Rank and display profiles based on the new cosine similarity score
    rank_and_display_profiles(data_concat, 'cosine_similarity_sbert')

if __name__ == '__main__':
    main()
