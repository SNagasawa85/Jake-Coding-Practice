class Queue:
    def __init__(self):
        self.items = []

# classmethods here
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

# define another class

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        # example flavors = ['cherry', 'chocolate', 'rocky road']
        self.orders = Queue()
# write 3 methods for this class: take_orders(), show_all_orders(), and next_orders()
# take_orders will pass 3 arguments aside from self: customer, flavor, and scoops
# customer and flavor will be strings and scoops will be integer

# take order method
    def take_order(self, customer, flavor, scoops):
      # example input (self, 'Josh', 'vanilla', 5)
      # make sure the shop has the flavor
      # step 1: iterate the list
      # step 2: compare flavor to each value as we iterate
      # if flavor == any value then we can move on in the order
      # if we don't find any that == flavor then we throw an error message
      goodFlavor = False
      for i in range (len(self.flavors)):
        if self.flavors[i] == flavor:
          goodFlavor = True
      if not goodFlavor:
        print('YOU NEED TO CHOOSE A DIFFERENT FLAVOR ASSHOLE!!!')
        return
      
      # only scoops that are between 1 and 3
      if scoops <= 0:
        print('you may only order between 1 and 3 scoops')
        return
      if scoops >= 3:
        print('you may only order between 1 and 3 scoops')
        return
      print('Order Created!')
      order = {
        'customer': customer,
        'flavor': flavor,
        'scoops': scoops,
      }
      self.orders.enqueue(order)
      

# show all orders method
    def show_all_orders(self):
      # if the length of the list is 0, then the list is empty and we have no pending orders
      if len(self.orders.items) == 0:
        print('No Pending Orders.')
      else:
        # if the length is not 0, then there are orders in the list, and we will print them by making a big string with everything for each order
        print('All Pending Ice Cream Orders:')
        for i in range (len(self.orders.items)):
          # here we iterate the list and we make one line that will print for each order that includes all the info for that order
          # the ' [i] ' refers to the index of the list, so with each iteration of the loop we touch the next value which is the next order
          print('Customer: ' + self.orders.items[i]['customer'] +' -- '+ 'Flavor: ' + self.orders.items[i]['flavor'] + 'Scoops: '+ ' -- ' + str(self.orders.items[i]['scoops']))


# next order method
    def next_order(self):
      if len(self.orders.items) == 0:
        print('no Orders')
        return
      # here we hold the order information in a variable
      orderUp = self.orders.items[0]
      # then we print out the order information
      print('Next Order Up!')
      print('Customer: ' + orderUp['customer'] + ' -- ' + 'Flavor: ' + orderUp['flavor'] + ' -- ' + 'Scoops: ' + str(orderUp['scoops']))
      # finally we remove the order we printed using the dequeue function
      self.orders.dequeue()

# Testing
shop1 = IceCreamShop(['chocolate', 'vanilla'])
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop1.take_order('Josh', 'mint chip', 2)
shop.take_order('Josh', 'mint chip', 2)
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
