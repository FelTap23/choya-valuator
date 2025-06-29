import yaml
from choya.validator.advanced_field_validator import AdvancedFieldValidator
from typing import Any


#Works fine for the MVP
#Check the generation for an schema
class InMemoryValidator(AdvancedFieldValidator):
    def __init__(self, node_name : str, filename : str):
        print(f"In Memory validator for {node_name}")
        self.node_name : str = node_name.lower()
        self.__valid_values : dict = self.load_file_yml(filename)[node_name]
        self.__fields_to_validate =  { key : set(self.__valid_values[key].keys())   for key in  self.__valid_values.keys() }
        
                
    def validate(self,field_name : str, input_value : Any) -> Any:
        allowed_values  = self.__fields_to_validate.get(field_name)
        if(allowed_values):
            if(input_value in allowed_values):
                return input_value
            else:
                raise ValueError(f"Invalid field name  {self.node_name}  {field_name}. The value: '{input_value}' is not allowed, allowed values {allowed_values}")    
        else:
            raise ValueError(f"Invalid field name {self.node_name} {field_name}. There are no values to validate it, please remove from validation list o check why its here")
    
    def load_file_yml(self,filename):
        with open(filename,"r") as file:
            yaml_file_content =  yaml.safe_load(file)
        return yaml_file_content

    def __str__(self):
        return str(self.__fields_to_validate)