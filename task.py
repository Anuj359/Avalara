######
    # Get synonyms, antonyms, and definitions for a given word from an API.

    # Args:
    #     word (str): The word to get information for.
    # Usage:
    #       python3 task.py word
    # Returns:
    #     dict: A dictionary containing synonyms, antonyms, and definitions.
####
import requests
import sys
import urllib3

# Uncomment to hard code the API_KEY and fetch definition to run python script
# def get_word_info(word):
#    api_key = 'XXXXXX'
#    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key}'

# Comment the below lines if not using Github actions
def get_word_info(word, api_key):

    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{word}?key={api_key}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        json_response = response.json()

        if json_response:
            word_info = {}
            if 'meta' in json_response[0]:
                meta = json_response[0]['meta']
                # Loop across json to find synonyms and antonyms
                if 'syns' in meta and 'ants' in meta:
                    word_info['synonyms'] = [synonym for syn_list in meta['syns'] for synonym in syn_list]
                    word_info['antonyms'] = [antonym for ant_list in meta['ants'] for antonym in ant_list]
                else:
                    word_info['synonyms'] = []
                    word_info['antonyms'] = []
            # Loop to fetch all the short definitions from the json
            word_info['definitions'] = list(set([d['shortdef'][0] for d in json_response if 'shortdef' in d]))
            return word_info

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

#Function to print the segregated data
def print_word_info(word, word_info):
    if word_info:
        print(f"Synonyms of {word}:")
        print(", ".join(word_info['synonyms']))
        print("\n")
        print(f"Antonyms of {word}:")
        print(", ".join(word_info['antonyms']))
        print("\n")
        
        if word_info['definitions']:
            print(f"The definitions of {word} are:")
            for i, definition in enumerate(word_info['definitions'], 1):
                print(f"{i}. {definition}")
        else:
            print(f"No definition found for {word}")
    else:
        print(f"No information found for {word}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a word as a command line argument")
        sys.exit(1)

    word = sys.argv[1]

# Comment below line of codes to use python script on terminal
    api_key = os.getenv('DICTIONARY_API_KEY')
    if not api_key:
        print("Dictionary API key not found.")
        sys.exit(1)

    word_info = get_word_info(word, api_key)
    
# Uncomment the below line to use python script on terminal
#    word_info = get_word_info(word)
    print_word_info(word, word_info)