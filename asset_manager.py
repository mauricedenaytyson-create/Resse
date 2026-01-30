"""AssetManager class for managing a collection of assets."""

import json
import os
from typing import List, Optional
from asset import Asset


class AssetManager:
    """Manages a collection of assets with CRUD operations."""
    
    def __init__(self, storage_file: str = "assets.json"):
        """
        Initialize the AssetManager.
        
        Args:
            storage_file: Path to the JSON file for storing assets
        """
        self.storage_file = storage_file
        self.assets: List[Asset] = []
        self.load_assets()
    
    def load_assets(self) -> None:
        """Load assets from the storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.assets = [Asset.from_dict(asset_data) for asset_data in data]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading assets: {e}")
                self.assets = []
        else:
            self.assets = []
    
    def save_assets(self) -> None:
        """Save assets to the storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump([asset.to_dict() for asset in self.assets], f, indent=2)
    
    def add_asset(self, asset: Asset) -> bool:
        """
        Add a new asset.
        
        Args:
            asset: The asset to add
            
        Returns:
            True if added successfully, False if asset_id already exists
        """
        if self.get_asset(asset.asset_id):
            return False
        self.assets.append(asset)
        self.save_assets()
        return True
    
    def get_asset(self, asset_id: str) -> Optional[Asset]:
        """
        Get an asset by ID.
        
        Args:
            asset_id: The ID of the asset to retrieve
            
        Returns:
            The asset if found, None otherwise
        """
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None
    
    def update_asset(self, asset_id: str, **kwargs) -> bool:
        """
        Update an asset's properties.
        
        Args:
            asset_id: The ID of the asset to update
            **kwargs: Properties to update (name, asset_type, value, purchase_date)
            
        Returns:
            True if updated successfully, False if asset not found
        """
        asset = self.get_asset(asset_id)
        if not asset:
            return False
        
        for key, value in kwargs.items():
            if hasattr(asset, key):
                setattr(asset, key, value)
        
        self.save_assets()
        return True
    
    def delete_asset(self, asset_id: str) -> bool:
        """
        Delete an asset.
        
        Args:
            asset_id: The ID of the asset to delete
            
        Returns:
            True if deleted successfully, False if asset not found
        """
        asset = self.get_asset(asset_id)
        if not asset:
            return False
        
        self.assets.remove(asset)
        self.save_assets()
        return True
    
    def list_assets(self) -> List[Asset]:
        """
        Get all assets.
        
        Returns:
            List of all assets
        """
        return self.assets
    
    def get_total_value(self) -> float:
        """
        Calculate the total value of all assets.
        
        Returns:
            Sum of all asset values
        """
        return sum(asset.value for asset in self.assets)
