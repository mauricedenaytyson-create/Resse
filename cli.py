#!/usr/bin/env python3
"""Command-line interface for the Asset Management System."""

import sys
from asset import Asset
from asset_manager import AssetManager


def print_help():
    """Print usage instructions."""
    print("""
Asset Management System - Command Line Interface

Usage:
    python cli.py <command> [arguments]

Commands:
    add <id> <name> <type> <value> [purchase_date]
        Add a new asset
        Example: python cli.py add A001 "Laptop" "Electronics" 1200.00 "2024-01-15"
    
    get <id>
        Get details of a specific asset
        Example: python cli.py get A001
    
    update <id> <field> <value>
        Update an asset's field (name, asset_type, value, purchase_date)
        Example: python cli.py update A001 value 1100.00
    
    delete <id>
        Delete an asset
        Example: python cli.py delete A001
    
    list
        List all assets
        Example: python cli.py list
    
    total
        Get total value of all assets
        Example: python cli.py total
    
    help
        Show this help message
    """)


def main():
    """Main CLI function."""
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1].lower()
    manager = AssetManager()
    
    try:
        if command == "add":
            if len(sys.argv) < 6:
                print("Error: add command requires <id> <name> <type> <value> [purchase_date]")
                return
            
            asset_id = sys.argv[2]
            name = sys.argv[3]
            asset_type = sys.argv[4]
            value = float(sys.argv[5])
            purchase_date = sys.argv[6] if len(sys.argv) > 6 else None
            
            asset = Asset(asset_id, name, asset_type, value, purchase_date)
            if manager.add_asset(asset):
                print(f"✓ Asset added successfully: {asset}")
            else:
                print(f"✗ Error: Asset with ID '{asset_id}' already exists")
        
        elif command == "get":
            if len(sys.argv) < 3:
                print("Error: get command requires <id>")
                return
            
            asset_id = sys.argv[2]
            asset = manager.get_asset(asset_id)
            if asset:
                print(asset)
            else:
                print(f"✗ Asset with ID '{asset_id}' not found")
        
        elif command == "update":
            if len(sys.argv) < 5:
                print("Error: update command requires <id> <field> <value>")
                return
            
            asset_id = sys.argv[2]
            field = sys.argv[3]
            value = sys.argv[4]
            
            # Convert value to appropriate type
            if field == "value":
                value = float(value)
            
            if manager.update_asset(asset_id, **{field: value}):
                print(f"✓ Asset '{asset_id}' updated successfully")
            else:
                print(f"✗ Asset with ID '{asset_id}' not found")
        
        elif command == "delete":
            if len(sys.argv) < 3:
                print("Error: delete command requires <id>")
                return
            
            asset_id = sys.argv[2]
            if manager.delete_asset(asset_id):
                print(f"✓ Asset '{asset_id}' deleted successfully")
            else:
                print(f"✗ Asset with ID '{asset_id}' not found")
        
        elif command == "list":
            assets = manager.list_assets()
            if assets:
                print(f"\nTotal Assets: {len(assets)}")
                print("-" * 80)
                for asset in assets:
                    print(asset)
                print("-" * 80)
                print(f"Total Value: ${manager.get_total_value():.2f}")
            else:
                print("No assets found")
        
        elif command == "total":
            total = manager.get_total_value()
            count = len(manager.list_assets())
            print(f"Total Assets: {count}")
            print(f"Total Value: ${total:.2f}")
        
        elif command == "help":
            print_help()
        
        else:
            print(f"Unknown command: {command}")
            print_help()
    
    except ValueError as e:
        print(f"✗ Error: Invalid value - {e}")
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
