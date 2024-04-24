#!/bin/bash

# Configuration
CSV_DIR="CSV"
DB_FILE="ahc-cemeteries.db"
DEVCONTAINER_DIR=".devcontainer"
DEVCONTAINER_JSON="$DEVCONTAINER_DIR/devcontainer.json"
DOCKERFILE="$DEVCONTAINER_DIR/Dockerfile"

# Check and install Datasette and dependencies
check_and_install_dependencies() {
    echo "Checking for Python and pip..."
    if ! command -v python3 &>/dev/null || ! command -v pip &>/dev/null; then
        echo "Python or pip is not installed. Installing them..."
        sudo apt-get update && sudo apt-get install python3 python3-pip -y
    else
        echo "Python and pip are installed."
    fi

    echo "Checking for Datasette..."
    if ! pip list 2>/dev/null | grep -q datasette; then
        echo "Datasette is not installed. Installing Datasette..."
        pip install datasette
    else
        echo "Datasette is installed."
    fi
}

# Check and prepare GitHub Codespaces configuration
prepare_codespaces_configuration() {
    echo "Checking GitHub Codespaces configuration..."

    # Check and create .devcontainer directory
    if [ ! -d "$DEVCONTAINER_DIR" ]; then
        mkdir $DEVCONTAINER_DIR
    fi

    # Create or overwrite the devcontainer.json
    if [ ! -f "$DEVCONTAINER_JSON" ]; then
        echo "Creating $DEVCONTAINER_JSON..."
        cat <<EOF >$DEVCONTAINER_JSON
{
  "name": "Datasette Environment",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "forwardPorts": [8001],
  "postCreateCommand": "bash setup.sh",
  "remoteUser": "vscode"
}
EOF
    fi

    # Create or overwrite the Dockerfile
    if [ ! -f "$DOCKERFILE" ]; then
        echo "Creating $DOCKERFILE..."
        cat <<EOF >$DOCKERFILE
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install Datasette and SpatiaLite dependencies
RUN pip install datasette datasette-cluster-map \
    && apt-get update \
    && apt-get install -y libsqlite3-mod-spatialite
EOF
    fi
}

# Import CSVs into SQLite
import_csvs_to_sqlite() {
    echo "Creating/Updating SQLite database from CSV files..."

    if [ -f "$DB_FILE" ]; then
        read -p "Database $DB_FILE already exists. Delete and create a new one? (y/N) " confirm
        if [[ "$confirm" =~ ^[Yy]$ ]]; then
            rm "$DB_FILE"
            echo "Deleted $DB_FILE."
        else
            echo "Aborted database overwrite."
            return
        fi
    fi

    # Navigate to CSV directory
    cd $CSV_DIR

    # Read header from first CSV to create a SQL CREATE TABLE statement
    IFS=',' read -ra HEADER <<< "$(head -n 1 ahc-cemeteries1.csv)"
    SQL="CREATE TABLE cemeteries ("
    for i in "${!HEADER[@]}"; do
        COLUMN_NAME=$(echo "${HEADER[$i]}" | sed 's/[^a-zA-Z0-9_]/_/g')
        SQL+="$COLUMN_NAME TEXT"
        if (( $i < ${#HEADER[@]} - 1 )); then
            SQL+=", "
        fi
    done
    SQL+=");"
    sqlite3 ../$DB_FILE "$SQL"

    # Import each CSV file
    for file in *.csv; do
        echo "Importing $file into SQLite database..."
        (echo ".mode csv"; echo ".import '$file' cemeteries") | sqlite3 ../$DB_FILE
    done

    # Navigate back
    cd ..

    echo "All CSV files have been imported."
}

# Launch Datasette and open in browser (adjust for local or Codespaces use)
launch_datasette() {
    echo "Launching Datasette server..."
    datasette serve $DB_FILE --host 0.0.0.0 --port 8001 &
    sleep 3  # Wait for server to start

    # Check if port 8001 is available
    if lsof -i:8001; then
        echo "ERROR: Port 8001 is already in use. Trying another port..."
        datasette serve $DB_FILE --host 0.0.0.0 --port 8002 &
        sleep 3  # Ensure the server has time to start
    fi

    # Check if we are running in Codespaces
    if [ -n "$CODESPACES" ]; then
        echo "Running in GitHub Codespaces, opening browser..."
        gp preview $(gp url 8001)
    else
        echo "Opening local web browser..."
        if command -v xdg-open &>/dev/null; then
            xdg-open http://localhost:8001/
        elif command -v open &>/dev/null; then
            open http://localhost:8001/
        else
            echo "Web browser command not found. Please manually open http://localhost:8001/"
        fi
    fi
}

# Main execution
check_and_install_dependencies
prepare_codespaces_configuration
import_csvs_to_sqlite
launch_datasette

echo "Setup complete. Your environment is ready!"
