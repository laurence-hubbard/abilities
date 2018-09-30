# abilities
A python library that helps provide quick insight into the libraries and classes you are working with. Specifically designed with Data Scientists using Jupyter Notebook in mind.

### How To Install
```sh
$ pip install git+https://github.com/laurence-hubbard/abilities.git
```
### How To Use
```python
from abilities import abilities
my_datascience_object = ...
abilities(my_datascience_object)
```
### Example

###### _Input_
```python
from abilities import abilities
mylist = [1,2,3]
abilities(mylist)
```
###### _Output_
> The key abilities of  <class 'list'>  are:
> append
> clear
> copy
> extend
> insert
> pop
> remove
> reverse
> sort
