from py_ms_cognitive import PyMsCognitiveWebSearch


def read_bing_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            # I've added .replace() since in Python 3.6 .readline()
            # returns str with \n at the end
            bing_api_key = f.readline().replace('\n', '')
    except:
        raise IOError('bing.key file not found!')

    return bing_api_key


def run_query(search_terms):
    bing_api_key = read_bing_key()
    if not bing_api_key:
        raise KeyError('Bing Key Not Found')
    results_per_page = 10

    results = []

    try:
        search_service = PyMsCognitiveWebSearch(bing_api_key, search_terms)
        response = search_service.search(limit=results_per_page, format='json')

        for result in response:
            results.append({
                'title': result.json['name'],
                'link': result.json['displayUrl'],
                'summary': result.json['snippet']})
    except:
        print("Error when querying the Bing API")

    return results


def main():
    query = input("Enter a query \n")
    results = run_query(query)
    for result in results:
        print(result['title'])
        print('-' * len(result['title']))
        print(result['summary'])
        print(result['link'])
        print()


if __name__ == '__main__':
    main()
