import module1
from module1 import nom_de_famille as ndf, function as fct

import builtins  

print(dir(builtins))
print(module1.__name__)
print(__name__)  #__main__

