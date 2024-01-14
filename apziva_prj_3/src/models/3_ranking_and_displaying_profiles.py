import pandas as pd
def rank_and_display_profiles(data_concat, column_name, top_n=7):
    ranked_profiles = data_concat.sort_values(by=column_name, ascending=False).head(top_n)
    print("Top {} Profiles:".format(top_n))
    print(ranked_profiles['data_concat'], '\n')
    return ranked_profiles
