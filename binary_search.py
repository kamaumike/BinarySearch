class BinarySearch(list):
  """The Binary Search class"""
  
  def __init__(self, a, b, *args):
    list.__init__(self, *args)
    self.length_of_list = a
    self.step = b
    upper_bound = self.length_of_list * self.step #value that determines upper bound for looping a list
    for i in range(self.step, upper_bound + 1, self.step):
      self.append(i)
            
  #Gets the length of the list        
  @property
  def length(self):
    return len(self)
        
  #Searches a value and returns a dictionary    
  def search(self, value, start=0, stop=None, count=0):
    if not stop:
      stop = self.length - 1
    if value == self[start]:
      return dict(count = count, index = start)
    elif value == self[stop]:
      return dict(count = count, index = stop)
  
    middle = (start + stop) // 2  #divide the list into half and search
    
    if value == self[middle]:
      return dict(count = count, index = middle)
    elif value > self[middle]:
      start = middle + 1
    elif value < self[middle]:
      stop = middle - 1
    if start >= stop:
      return dict(count = count, index = -1)
    count += 1  
    return self.search(value, start, stop, count)