#!/usr/bin/env python3
"""Example usage of the Asset Management System."""

from asset import Asset
from asset_manager import AssetManager


def main():
    """Demonstrate the asset management system."""
    print("=== Asset Management System - Example Usage ===\n")
    
    # Create a new asset manager
    manager = AssetManager("example_assets.json")
    
    # Add some assets
    print("1. Adding assets...")
    assets_to_add = [
        Asset("A001", "MacBook Pro", "Electronics", 2500.00, "2024-01-15"),
        Asset("A002", "Office Desk", "Furniture", 450.00, "2024-02-20"),
        Asset("A003", "Ergonomic Chair", "Furniture", 350.00, "2024-02-20"),
        Asset("A004", "Monitor", "Electronics", 600.00, "2024-03-10"),
    ]
    
    for asset in assets_to_add:
        if manager.add_asset(asset):
            print(f"  ✓ Added: {asset.name}")
        else:
            print(f"  ✗ Failed to add: {asset.name} (already exists)")
    
    # List all assets
    print("\n2. Listing all assets...")
    for asset in manager.list_assets():
        print(f"  {asset}")
    
    # Get total value
    print(f"\n3. Total value of all assets: ${manager.get_total_value():.2f}")
    
    # Get a specific asset
    print("\n4. Getting asset A001...")
    asset = manager.get_asset("A001")
    if asset:
        print(f"  Found: {asset}")
    
    # Update an asset
    print("\n5. Updating asset A001 value to $2300...")
    if manager.update_asset("A001", value=2300.00):
        print("  ✓ Update successful")
        updated_asset = manager.get_asset("A001")
        print(f"  Updated: {updated_asset}")
    
    # Delete an asset
    print("\n6. Deleting asset A004...")
    if manager.delete_asset("A004"):
        print("  ✓ Deletion successful")
    
    # List remaining assets
    print("\n7. Listing remaining assets...")
    for asset in manager.list_assets():
        print(f"  {asset}")
    
    print(f"\n8. Final total value: ${manager.get_total_value():.2f}")
    print("\n=== Example Complete ===")


if __name__ == "__main__":
    main()
