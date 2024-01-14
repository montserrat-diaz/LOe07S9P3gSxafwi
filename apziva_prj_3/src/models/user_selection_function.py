# Function for prompting user to select a profile
def select_and_display_profile(data_concat):
    # Prompt user to select a profile
    selected_index = int(input("Enter the index of the profile you want to select: "))
    
    # Filter the DataFrame based on the selected index
    selected_profile = data_concat['data_concat'].iloc[selected_index]

    # Display the selected profile
    print("\nSelected Profile:")
    print(selected_profile)
    return selected_profile
