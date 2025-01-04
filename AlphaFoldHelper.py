import requests
import json
import os
from datetime import datetime

def fetch_models_by_uniprot(uniprot_accession):
    """Fetch models by UniProt accession."""
    url = f"https://www.alphafold.ebi.ac.uk/api/prediction/{uniprot_accession}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        file_name = f"{uniprot_accession}_models.json"
        with open(file_name, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {file_name}")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def fetch_summary_by_residue_range(uniprot_accession, residue_range):
    """Fetch summary data by residue range."""
    url = f"https://www.alphafold.ebi.ac.uk/api/uniprot/summary/{uniprot_accession}.json?range={residue_range}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        summary_data = response.json()
        file_name = f"{uniprot_accession}_summary_{residue_range.replace('-', '_')}.json"
        with open(file_name, "w") as f:
            json.dump(summary_data, f, indent=4)
        print(f"Summary data saved to {file_name}")
        return summary_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching summary: {e}")
        return None

def download_model_files(data, uniprot_accession):
    """Download structure and related files from the API response."""
    save_dir = f"{uniprot_accession}_files"
    os.makedirs(save_dir, exist_ok=True)

    for entry in data:
        for file_type in ["cifUrl", "bcifUrl", "pdbUrl", "paeImageUrl", "paeDocUrl"]:
            file_url = entry.get(file_type)
            if file_url:
                file_name = os.path.join(save_dir, file_url.split("/")[-1])
                try:
                    print(f"Downloading {file_url}...")
                    file_response = requests.get(file_url)
                    file_response.raise_for_status()
                    with open(file_name, "wb") as f:
                        f.write(file_response.content)
                    print(f"Saved {file_name}")
                except requests.exceptions.RequestException as e:
                    print(f"Error downloading {file_url}: {e}")

def process_data(data):
    """Extract and display relevant information from the API response."""
    detailed_info = []
    for entry in data:
        entry_info = {
            "Entry ID": entry.get("entryId"),
            "Gene": entry.get("gene"),
            "Organism": entry.get("organismScientificName"),
            "Sequence Length": len(entry.get("uniprotSequence", "")),
            "Model Created Date": entry.get("modelCreatedDate"),
            "Latest Version": entry.get("latestVersion"),
            "Structure Files": {
                file_type: entry.get(file_type) for file_type in ["cifUrl", "bcifUrl", "pdbUrl"] if entry.get(file_type)
            },
        }
        detailed_info.append(entry_info)
        print(json.dumps(entry_info, indent=4))
    return detailed_info

def analyze_and_save_data(data, uniprot_accession):
    """Save detailed information to a file."""
    analysis_file = f"{uniprot_accession}_analysis.json"
    try:
        with open(analysis_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Detailed analysis saved to {analysis_file}")
    except IOError as e:
        print(f"Error saving analysis: {e}")

def main():
    print("AlphaFold Protein Structure Database API Client")
    uniprot_accession = input("Enter UniProt accession (e.g., P00520): ")
    action = input("Choose an action:\n1. Fetch models by UniProt accession\n2. Fetch summary by residue range\n3. Fetch and analyze all\nEnter your choice (1/2/3): ")

    if action == "1":
        data = fetch_models_by_uniprot(uniprot_accession)
        if data:
            processed_data = process_data(data)
            analyze_and_save_data(processed_data, uniprot_accession)
            download_action = input("Do you want to download structure files? (yes/no): ").strip().lower()
            if download_action == "yes":
                download_model_files(data, uniprot_accession)

    elif action == "2":
        residue_range = input("Enter residue range (e.g., 1-100): ")
        fetch_summary_by_residue_range(uniprot_accession, residue_range)

    elif action == "3":
        data = fetch_models_by_uniprot(uniprot_accession)
        if data:
            processed_data = process_data(data)
            analyze_and_save_data(processed_data, uniprot_accession)
            download_model_files(data, uniprot_accession)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
