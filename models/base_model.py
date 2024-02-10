#!/usr/bin/python3
""" 
Defines the BaseModel class
which is the parent class for all classes in this project.
"""
from datetime import datetime
from uuid import uuid4

class BaseModel():
    """The parent class for my AirBnB clone project."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        date_form = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(v, date_form))
                else:
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid.uuid4()))
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance.

        A key __class__ is added to the dictionary with the class name of the object.
        created_at and updated_at are converted to string object in ISO format.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
