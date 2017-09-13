import json
import urllib
import urllib2

def read_api_key(key_file_name):
    """
    Reads the API key from a file called key_file_name.
    Returns either None (no key found), or a string representing the key.
    Remember: put *.key in your .gitignore file to avoid committing it!
    """
    # See Python Anti-Patterns - it's an awesome resource!
    # Here we are using "with" when opening files.
    # http://docs.quantifiedcode.com/python-anti-patterns/maintainability/

    api_key = None

    try:
        with open(key_file_name, 'r') as f:
            api_key = f.readline().strip()
    except:
        raise IOError( '{0} file not found'.format(key_file_name))

    return api_key

def run_query(search_terms, size=10):
    """
    Given a string containing search terms (query), and a number of results to return (default of 10),
    returns a list of results from the Webhose API, with each result consisting of a title, link and summary.
    """
    api_key = read_api_key('chatnoir.key')

    if not api_key:
        raise KeyError('API key not found')


    # What's the base URL for the Webhose API?
    root_url = 'https://www.chatnoir.eu/api/v1/_search'

    # Format the query string - escape special characters.
    query_string = urllib.quote(search_terms)

    # Use string formatting to construct the complete API URL.
    search_url ='{root_url}?apikey={key}&query={query}&index=cc1511&size={size}'.format(
                    root_url=root_url,
                    key=api_key,
                    query=query_string,
                    size=size)

    results = []

    try:
        # Connect to the ChatNoir API, and convert the response to a Python dictionary.
        print(search_url)
        response = urllib2.urlopen(search_url).read()
        #print(response)
        json_response = json.loads(response)

        # Loop through the posts, appendng each to the results list as a dictionary.
        for post in json_response['results']:
            #print(post['title'])
            results.append({'title': post['title'],
                            'link': post['target_uri'],
                            'summary': post['snippet'][:200]})
    except Exception as e:
        print(e)
        print("Error when querying the Chatnoir API")

    # Return the list of results to the calling function.
    return results


def main():
    print("Enter a query ")
    query = raw_input()
    results = run_query(query)
    for result in results:
        print(result['title'])
        print('-'*len(result['title']))
        print(result['summary'])
        print(result['link'])
        print()


if __name__ == '__main__':
    main()