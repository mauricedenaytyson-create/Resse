"""Asset class for managing individual assets."""

from datetime import datetime
from typing import Optional
import re


class Asset:
    """Represents a single asset with its properties."""
    
    def __init__(
        self,
        asset_id: str,
        name: str,
        asset_type: str,
        value: float,
        purchase_date: Optional[str] = None
    ):
        """
        Initialize an Asset.
        
        Args:
            asset_id: Unique identifier for the asset
            name: Name of the asset
            asset_type: Type/category of the asset
            value: Monetary value of the asset (must be non-negative)
            purchase_date: Date of purchase (ISO format: YYYY-MM-DD)
        
        Raises:
            ValueError: If value is negative or date format is invalid
        """
        if value < 0:
            raise ValueError(f"Asset value must be non-negative, got {value}")
        
        if purchase_date:
            self._validate_date_format(purchase_date)
        
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.value = value
        self.purchase_date = purchase_date or datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def _validate_date_format(date_str: str) -> None:
        """Validate that date is in YYYY-MM-DD format."""
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, date_str):
            raise ValueError(f"Date must be in YYYY-MM-DD format, got '{date_str}'")
    
    def to_dict(self) -> dict:
        """Convert asset to dictionary format."""
        return {
            "asset_id": self.asset_id,
            "name": self.name,
            "asset_type": self.asset_type,
            "value": self.value,
            "purchase_date": self.purchase_date
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Asset":
        """Create an Asset from a dictionary."""
        return cls(
            asset_id=data["asset_id"],
            name=data["name"],
            asset_type=data["asset_type"],
            value=data["value"],
            purchase_date=data.get("purchase_date")
        )
    
    def __str__(self) -> str:
        """String representation of the asset."""
        return (
            f"Asset(id={self.asset_id}, name={self.name}, "
            f"type={self.asset_type}, value=${self.value:.2f}, "
            f"purchase_date={self.purchase_date})"
        )
