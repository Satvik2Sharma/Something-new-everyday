import pandas as pd
import re

INPUT_CSV = "Springer_Nature_3667.csv"
OUTPUT_RIS = "Springer_Nature_3667.ris"

df = pd.read_csv(INPUT_CSV)

with open(OUTPUT_RIS, "w", encoding="utf-8") as ris:

    for _, row in df.iterrows():

        # RIS Type
        ris.write("TY  - JOUR\n")

        # Title
        if pd.notna(row.get("Item Title")):
            ris.write(f"TI  - {row['Item Title']}\n")

        # Journal
        if pd.notna(row.get("Publication Title")):
            ris.write(f"JO  - {row['Publication Title']}\n")

        # Volume
        if pd.notna(row.get("Journal Volume")):
            ris.write(f"VL  - {row['Journal Volume']}\n")

        # Issue
        if pd.notna(row.get("Journal Issue")):
            ris.write(f"IS  - {row['Journal Issue']}\n")

        # Year
        if pd.notna(row.get("Publication Year")):
            ris.write(f"PY  - {int(row['Publication Year'])}\n")

        # DOI
        if pd.notna(row.get("Item DOI")):
            ris.write(f"DO  - {row['Item DOI']}\n")

        # URL
        if pd.notna(row.get("URL")):
            ris.write(f"UR  - {row['URL']}\n")

        # Authors
        authors = str(row.get("Authors", "")).strip()

        if authors and authors.lower() != "nan":

            # Springer sometimes exports authors without separators.
            # This regex attempts to split before capitalized names.
            split_authors = re.findall(
                r"[A-Z][a-zA-Z\-\']+(?:\s+[A-Z][a-zA-Z\-\']+)+",
                authors
            )

            if split_authors:
                for author in split_authors:
                    ris.write(f"AU  - {author.strip()}\n")
            else:
                ris.write(f"AU  - {authors}\n")

        ris.write("ER  - \n\n")

print(f"RIS file saved as: {OUTPUT_RIS}")
