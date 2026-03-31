import shodan
import json
import time

API_KEY = "YOUR_API_KEY"
api = shodan.Shodan(API_KEY)

# War-related countries
queries = [
    "country:UA",
    "country:RU",
    "country:IL",
    "country:IR"
]

MAX_PAGES = 5   # increase for more data (each page ~100 results)

all_data = []

for query in queries:
    print(f"\n[+] Collecting data for: {query}")

    for page in range(1, MAX_PAGES + 1):
        try:
            results = api.search(query, page=page)

            for result in results['matches']:
                entry = {
                    "ip": result.get("ip_str"),
                    "country": result.get("location", {}).get("country_name"),
                    "port": result.get("port"),
                    "org": result.get("org", "n/a"),
                    "isp": result.get("isp", "n/a"),
                    "hostnames": result.get("hostnames"),
                    "timestamp": result.get("timestamp"),
                    "product": result.get("product"),
                    "version": result.get("version"),
                    "vulns": list(result.get("vulns", []))
                }
                all_data.append(entry)

            print(f"   Page {page} collected")

            time.sleep(1)  # avoid rate limits

        except Exception as e:
            print(f"[!] Error on page {page}: {e}")
            break

# Save JSON
with open("war_shodan_data.json", "w") as f:
    json.dump(all_data, f, indent=4)

print(f"\n✅ Total records collected: {len(all_data)}")
