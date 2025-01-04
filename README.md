# AlphaFold Helper

AlphaFold Helper is a Python-based tool designed to interact with the AlphaFold Protein Structure Database API. It allows users to retrieve and process detailed information about AlphaFold protein structure predictions, including metadata, sequence details, structure models, and various related files.

## Features

- Fetch models by UniProt accession.
- Retrieve detailed metadata for each protein structure.
- Download and organize structure files (PDB, CIF, and bCIF).
- Retrieve predicted aligned error (PAE) files and images.
- Automatically save and organize data in structured directories.
- Extensive error handling and user feedback.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RohanNathHERE/alphafold-helper.git
   cd alphafold-helper
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage

Run the script interactively to fetch and process protein structure data:

```bash
python AlphaFoldHelper.py
```

### Example Interaction

1. Enter the UniProt accession when prompted:
   ```
   Enter UniProt accession (e.g., P00520): P00520
   ```
2. Choose an action:
   - Fetch models by UniProt accession.
   - Fetch summary by residue range.

3. View results and process data. The script will download files and save them locally in a structured format.

### Output

The script organizes output data as follows:

- **Metadata**: Saved as JSON files for easy analysis.
- **Structure Files**: Downloads PDB, CIF, and bCIF files to designated directories.
- **PAE Files**: Saves aligned error images and JSON files.

## File Structure

```
AlphaFoldHelper/
├── data/
│   ├── P00520/
│   │   ├── metadata.json
│   │   ├── structure.pdb
│   │   ├── structure.cif
│   │   ├── pae_image.png
│   │   └── pae_data.json
├── AlphaFoldHelper.py
├── requirements.txt
└── README.md
```

## API Reference

The script utilizes the AlphaFold Protein Structure Database API:

- **GET /prediction/{qualifier}**: Retrieve all models for a UniProt accession.
- **GET /uniprot/summary/{qualifier}.json**: Fetch summary details for a UniProt residue range.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests to enhance this tool.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/)
- [UniProt](https://www.uniprot.org/)

## Contact

For questions or support, please contact:
- **Rohan Nath**: [rohann20@iiserbpr.ac.in](mailto:rohann20@iiserbpr.ac.in)
- GitHub: [https://github.com/RohanNathHERE](https://github.com/RohanNathHERE)
