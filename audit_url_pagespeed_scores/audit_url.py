from audit_scores import get_urls
import requests
import pandas as pd

final_urls = get_urls()[1:]

scores = {key: [] for key in ["Country","URL","Score"]}

key = key = 'INSERT KEY'

for url in final_urls:

    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={key}"

    response = requests.get(api_url)

    response = response.json()

    try:
        overall_score = (
            response["lighthouseResult"]["categories"]["performance"]["score"] * 100
        )

    except (KeyError, TypeError):
        # print("\nError \n" + url)
        continue

    # print("\n" + url + "\n" + str(overall_score))

    scores['Score'].append(overall_score)
    scores['URL'].append(url)

df = pd.DataFrame(scores)

print(df)