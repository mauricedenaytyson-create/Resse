# Resse

A simple and efficient Asset Management System for tracking and managing your assets.

## Features

- **Add Assets**: Create new assets with unique IDs, names, types, values, and purchase dates
- **View Assets**: Retrieve details of specific assets or list all assets
- **Update Assets**: Modify asset properties like name, type, value, or purchase date
- **Delete Assets**: Remove assets from the system
- **Calculate Total Value**: Get the total value of all tracked assets
- **Persistent Storage**: Assets are saved to a JSON file for persistence

## Installation

No external dependencies required! This project uses only Python standard library.

Requirements:
- Python 3.7 or higher

Clone the repository:
```bash
git clone https://github.com/mauricedenaytyson-create/Resse.git
cd Resse
```

## Usage

### Command Line Interface

The CLI provides an easy way to manage assets from the command line.

#### Add an Asset
```bash
python cli.py add <id> <name> <type> <value> [purchase_date]
```
Example:
```bash
python cli.py add A001 "Laptop" "Electronics" 1200.00 "2024-01-15"
```

#### View a Specific Asset
```bash
python cli.py get <id>
```
Example:
```bash
python cli.py get A001
```

#### Update an Asset
```bash
python cli.py update <id> <field> <value>
```
Example:
```bash
python cli.py update A001 value 1100.00
```

#### Delete an Asset
```bash
python cli.py delete <id>
```
Example:
```bash
python cli.py delete A001
```

#### List All Assets
```bash
python cli.py list
```

#### Get Total Value
```bash
python cli.py total
```

#### Help
```bash
python cli.py help
```

### Python API

You can also use the asset management system directly in your Python code:

```python
from asset import Asset
from asset_manager import AssetManager

# Create a manager
manager = AssetManager()

# Add an asset
laptop = Asset("A001", "MacBook Pro", "Electronics", 2500.00, "2024-01-15")
manager.add_asset(laptop)

# Get an asset
asset = manager.get_asset("A001")
print(asset)

# Update an asset
manager.update_asset("A001", value=2300.00)

# List all assets
for asset in manager.list_assets():
    print(asset)

# Get total value
total = manager.get_total_value()
print(f"Total: ${total:.2f}")

# Delete an asset
manager.delete_asset("A001")
```

### Example Script

Run the example script to see the system in action:

```bash
python example.py
```

This will demonstrate all the main features of the asset management system.

## Project Structure

```
Resse/
├── asset.py           # Asset class definition
├── asset_manager.py   # AssetManager class for CRUD operations
├── cli.py            # Command-line interface
├── example.py        # Example usage script
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Data Storage

Assets are stored in a JSON file (`assets.json` by default). The file is created automatically when you add your first asset.

Example JSON structure:
```json
[
  {
    "asset_id": "A001",
    "name": "MacBook Pro",
    "asset_type": "Electronics",
    "value": 2500.0,
    "purchase_date": "2024-01-15"
  }
]
```

## License

This project is open source and available under the MIT License.