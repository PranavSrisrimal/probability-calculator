import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents=[]
    for key,value in kwargs.items():
      j = value
      while (j>0) :
        self.contents.append(key)
        j -= 1 

  def draw(self, num_drawn):
        if num_drawn > len(self.contents):
            return self.contents
        chosen = []
        for i in range(num_drawn):
            choice = random.randint(0,(len(self.contents)-1))
            chosen.append(self.contents[choice])
            self.contents.remove(self.contents[choice])
        return chosen
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # count variable to denote success or failure 
  count=0
  for i in range(num_experiments) :

    hat_copy = copy.deepcopy(hat)
    copy_expected = copy.deepcopy(expected_balls)
    chosen_balls = hat_copy.draw(num_balls_drawn)
    
    #to check if drawn balls meet expected balls condition
    y=0
    for _ in copy_expected :
        y += copy_expected[_]
    
    #points to calculate how many right balls drawn (maybe greater than expected)
    points=0
    for chosen_ball in chosen_balls:
        if chosen_ball in copy_expected and copy_expected[chosen_ball]!=0 :
          
          points += 1
          copy_expected[chosen_ball] -= 1

    if y <= points :
      count += 1

  return count/num_experiments    
  

