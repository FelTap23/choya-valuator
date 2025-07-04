import yaml
from choya.validator.advanced_field_validator import AdvancedFieldValidator
from typing import Any


#Works fine for the MVP
#Check the generation for an schema
#Check the logs
class InMemoryValidator(AdvancedFieldValidator):
    def __init__(self, node_name : str, filename : str):
        self.filename = filename
        self.node_name : str = node_name.lower()
        self.__valid_values : dict = self.load_file_yml(filename)[node_name]
        self.__fields_to_validate :dict =  { key : set(self.__valid_values[key].keys())   for key in  self.__valid_values.keys() }
                    
    def validate(self,field_name : str, input_value : Any) -> bool:
        allowed_values : set  = self.__fields_to_validate.get(field_name)
        if(allowed_values):
            if(input_value in allowed_values):
                return True
            else:
                raise ValueError(f"Validation error on '{self.node_name}.{field_name}': received '{input_value}', expected one of {allowed_values}.")    
        else:
            raise ValueError(f"Invalid field name {self.node_name} {field_name}. No values were found for validation, but the field was marked for validation. Please review the schema and the validation data source  {self.filename} to identify any mismatch.")
    
    def load_file_yml(self,filename):
        with open(filename,"r") as file:
            yaml_file_content =  yaml.safe_load(file)
        return yaml_file_content
    
    def get_set_of_allowed_values(self,field_name) -> set:
        return self.__fields_to_validate.get(field_name)

    def __str__(self):
        return str(self.__fields_to_validate)