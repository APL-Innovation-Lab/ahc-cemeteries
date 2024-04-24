# AHC Cemeteries Data Repository

Welcome to the `ahc-cemeteries` repository, part of the APL Innovation Lab GitHub Organization. This repository is designed to facilitate the exploration and management of cemetery data through Datasette, an open-source multi-tool for exploring and publishing data. Our setup utilizes GitHub Codespaces to provide a seamless and easy-to-navigate development environment.

## Codespaces

Before you start, ensure you have access to GitHub Codespaces, which requires a GitHub account with appropriate permissions within the APL Innovation Lab organization.

## Setup

Whenever you initiate a Codespace for this repository, execute the `start.sh` script, with `bash start.sh`. This script manages the installation of dependencies, prepares the development environment, and loads the cemetery data into a SQLite database using Datasette.

### What the `start.sh` Script Does

- **Checks and installs Python and pip:** Necessary tools for running the Datasette server.
- **Installs Datasette and its dependencies:** Ensures you have Datasette installed within the Codespace environment.
- **Prepares GitHub Codespaces configuration:** Sets up the `.devcontainer` environment to ensure compatibility with the Codespaces setup.
- **Imports cemetery data from CSV files into SQLite:** If fresh data needs to be loaded or a new database needs to be created, this script handles it.
- **Launches Datasette:** After setting up, Datasette will serve the SQLite database at a designated port, which can be accessed directly within Codespaces.

### Getting Started

1. **Open your Codespace:** Navigate to the GitHub repository and open it in Codespaces. The `start.sh` script runs automatically.
2. **Run the Datasette server:** Once the initial setup completes, Datasette will be available, and your browser within Codespaces will automatically open the Datasette interface. If you're running locally, you may need to open the browser manually at `http://localhost:8001`.

### Using the Datasette Interface

Datasette provides a user-friendly web interface to explore the cemetery data. You can execute SQL queries, view table data, and even visualize geospatial data if included.

### Commands You Might Need

If you need to restart the Datasette server or re-import the data, you can use the following commands in the terminal:
- To start Datasette manually: `datasette serve ahc-cemeteries.db --host 0.0.0.0 --port 8001`
- To re-import the CSVs into the SQLite database: Navigate to the CSV directory and run the import commands outlined in the script.

## Support

If you encounter any issues or have questions about navigating or using the Codespaces environment with this repository, please file an issue in this GitHub repository or contact the APL Innovation Lab team.

## Contributing

We welcome contributions to improve the repository or enhance the data exploration tools. Please read our CONTRIBUTING guidelines before making a pull request.

Thank you for contributing to and using the AHC Cemeteries Data Repository!
