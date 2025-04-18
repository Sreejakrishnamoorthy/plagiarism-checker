from plagiarismchecker.algorithm import ConsineSim
from duckduckgo_search import DDGS  # Import DuckDuckGo search module

def searchWeb(text, output, c):
    """Search for text similarity using DuckDuckGo API instead of Google."""
    try:
        maxSim = 0
        itemLink = ''
        
        # Fetch search results using DuckDuckGo API
        with DDGS() as ddgs:
            results = list(ddgs.text(text, max_results=5))  # Get top 5 results

        if results:
            for item in results:
                content = item['body']  # Extract content snippet
                simValue = ConsineSim.cosineSim(text, content)  # Compute similarity
                
                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item['href']  # Get URL of result
                
                if item['href'] in output:
                    itemLink = item['href']
                    break

            # Store similarity results
            if itemLink in output:
                print('if', maxSim)
                output[itemLink] += 1
                c[itemLink] = ((c[itemLink] * (output[itemLink] - 1) + maxSim) / output[itemLink])
            else:
                print('else', maxSim)
                print(text)
                print(itemLink)
                output[itemLink] = 1
                c[itemLink] = maxSim

    except Exception as e:
        print(f"Error processing query: {text}")
        print("Error:", e)
        return output, c, 1  # Indicate failure

    return output, c, 0  # Indicate success
