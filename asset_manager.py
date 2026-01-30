"""AssetManager class for managing a collection of assets."""

import json
import os
import logging
from typing import List, Optional
from asset import Asset

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
            except (json.JSONDecodeError, KeyError, ValueError) as e:
                logger.error(f"Error loading assets from {self.storage_file}: {e}")
                logger.warning("Starting with empty asset list")
                self.assets = []
        else:
            self.assets = []
    
    def save_assets(self) -> None:
        """Save assets to the storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([asset.to_dict() for asset in self.assets], f, indent=2)
        except IOError as e:
            logger.error(f"Error saving assets to {self.storage_file}: {e}")
            raise
    
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
            
        Raises:
            ValueError: If an invalid field name is provided or validation fails
        """
        # Whitelist of allowed fields
        allowed_fields = {'name', 'asset_type', 'value', 'purchase_date'}
        
        # Check for invalid field names
        invalid_fields = set(kwargs.keys()) - allowed_fields
        if invalid_fields:
            raise ValueError(f"Invalid field name(s): {', '.join(invalid_fields)}")
        
        asset = self.get_asset(asset_id)
        if not asset:
            return False
        
        # Validate value and date if provided
        if 'value' in kwargs and kwargs['value'] < 0:
            raise ValueError(f"Asset value must be non-negative, got {kwargs['value']}")
        
        if 'purchase_date' in kwargs:
            asset._validate_date_format(kwargs['purchase_date'])
        
        for key, value in kwargs.items():
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
