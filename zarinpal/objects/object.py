from json import dumps


class Object:
    
    def to_dict(self):
        return  {
            key: value for key, value in self.__dict__.items() if value is not None
        }
   
    def __repr__(self):
        return dumps(self.to_dict(), ensure_ascii=False, indent=4)
    
    def __setitem__(self, key, value):
        setattr(self, key, value) 
  
    def __getitem__(self, item):
        return getattr(self, item)
 