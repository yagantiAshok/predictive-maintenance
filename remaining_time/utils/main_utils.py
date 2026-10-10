

from box import ConfigBox
import os 
import numpy as np 
import sys 
import yaml
from remaining_time.logger import logger
from remaining_time.exception import CustomException
from pathlib import Path
import joblib
from typing import Any

def read_yaml(filepath:str)->ConfigBox:
    "This function read the yaml and convert into Box Object"
    path = Path(filepath)
    try:
        if not path.exists():
            raise FileNotFoundError(f"Yaml file is not created {path}")
        with open(path,"r") as file:
            contents = yaml.safe_load(file) or {}
            logger.info("loaded yaml filepath")
            return ConfigBox(contents)
    except Exception as e:
        raise CustomException(e,sys)

def write_to_yaml(data:Any,filepath)->None:
    "This function converts our data into yaml file"
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        with open(path,"w") as file:
            yaml.dump(data=data,filepath=file,default_flow_style=False,sort_keys=False)
        logger.info("Data Saved into yaml file")
    except Exception as e:
        raise CustomException(e,sys)

def save_to_numpy(data:np.ndarray,filepath:str)->None:
    "save data in numpy type"
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        if path.suffix!=".npy":
            path = path.with_suffix(".npy")
        np.save(path,data)
        logger.info("succesfully saved the data into numpy")
    except Exception as e:
        raise CustomException(e,sys)

def load_numpy_data(filepath:str)->np.ndarray:
    "load the data into original format"
    path = Path(filepath)
    try:
        if not path.exists():
            raise FileNotFoundError(f"Filepth Not Exists :{path}")
        data = np.load(file=path)
        logger.info(f"Numpy data loaded from file {path}")
        return data
    except Exception as e:
        raise CustomException(e,sys)

def save_to_binary(data:Any,filepath:str)->None:
    "This function saves the data into binary format"
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        if path.suffix=="":
            path = path.with_suffix(".joblib")
        joblib.dump(value=data,filename=path)
    except Exception as e:
         raise CustomException(e,sys)

def load_binary_data(filepath)->Any:

    path = Path(filepath)
    try:
        if not path.exists():
            raise FileNotFoundError(f"File not present at : {path}")
        data = joblib.load(filename=path)
        return data
    except Exception as e:
        raise CustomException(e,sys)

def create_filepath(filepath:str)->None:
    "this function create directories and file even if we give only directories it still create"
    path = Path(filepath)
    try:
        if path.suffix:
            target_dir = path.parent
        else:
            target_dir = path
        path.mkdir(parents=True,exist_ok=True)
        logger.info(f"Directories created {target_dir}")

        if path.exists:
            path.touch(exist_ok=True)
            logger.info(f"File created {path}")

    except Exception as e:
        raise CustomException(e,sys)

def create_filepath(filepath:str)->None:
    "this function create directories and file even if we give only directories it still create"
    path = Path(filepath)
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        logger.info(f"Directories created {path}")
        if path.exists:
            path.touch(exist_ok=True)
            logger.info(f"File created {path}")

    except Exception as e:
        raise CustomException(e,sys)

