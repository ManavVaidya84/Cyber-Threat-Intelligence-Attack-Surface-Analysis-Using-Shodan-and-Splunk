import pandas as pd

df = pd.read_json("war_shodan_data.json")

# Optional: clean data
df['vulns'] = df['vulns'].apply(lambda x: ', '.join(x) if isinstance(x, list) else '')

df.to_csv("war_shodan_data.csv", index=False)

print("✅ CSV ready for Splunk!")
