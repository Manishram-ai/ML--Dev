import sys
import os
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransfromationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransfromation:
    def __init__(self):
        self.data_transformation_config = DataTransfromationConfig()

    def get_data_transformer():
        try:
            num_columns = ["writing_score", 'reading_score']

            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_pipline = Pipeline(
                steps=[
                    ("Simple imputer", SimpleImputer(strategy='median')),
                    ("scalar", StandardScaler())
                ]
            )

            cat_pipline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer()),
                    ("One Hot Encoding", OneHotEncoder()),
                    ("scale", StandardScaler())
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {num_columns}")

            preprocessor = ColumnTransformer(
                [
                    ('num_pipline', num_pipline, num_columns),
                    ("cat_pipline", cat_pipline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
