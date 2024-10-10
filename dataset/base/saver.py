import os
import pickle
import numpy as np
from copy import deepcopy
from base.utils import sitk_save


# Define default paths for saving data
PATH_DICT = {
    'image': 'images/{}.nii.gz'
}



class Saver:
    """
    Class for saving processed data, including images, projections, and blocks.
    
    Attributes:
        _path_dict (dict): Dictionary mapping data types to file paths.
        _projs_list (list): List of projection data.
        _projs_max (float): Maximum projection value for normalization.
        _is_blocks_coords_saved (bool): Flag indicating if block coordinates have been saved.
    """
    
    def __init__(self, root_dir, path_dict):
        """
        Initialize the Saver with a root directory and path dictionary.
        
        Args:
            root_dir (str): Root directory where data will be saved.
            path_dict (dict): Dictionary mapping data types to relative file paths.
        """
        self._path_dict = deepcopy(path_dict)
        for key in self._path_dict.keys():
            path = os.path.join(root_dir, self._path_dict[key])
            os.makedirs(os.path.dirname(path), exist_ok=True)
            self._path_dict[key] = path
        
        self._projs_list = []
        self._projs_max = 0.0
        self._is_blocks_coords_saved = False
    
    
    @property
    def path_dict(self):
        """
        Get the dictionary of data paths.
        
        Returns:
            dict: Dictionary of data paths.
        """
        
        return self._path_dict
    
    
    def _save_CT(self, data):
        """
        Save the processed CT image.
        
        Args:
            data (dict): Data dictionary containing 'name', 'image', and 'spacing'.
        """
        name = data['name']
        sitk_save(
            self._path_dict['image'].format(name),
            image=data['image'],
            spacing=data['spacing'],
            uint8=True  # Save as uint8 image
        )
    
    
    def save(self, data):
        """
        Save all data components for a single data item.
        
        Args:
            data (dict): Data dictionary containing all necessary data.
        """
        self._save_CT(data)
