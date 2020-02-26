from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    # def __init__(self, limit=10):
    #     self.limit = limit
    #     self.size = 0
    #     self.cache = DoublyLinkedList()
    #     self.storage = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    # def get(self, key):
    #     if key in self.storage:
    #         # node = self.cache.find_value(key)
    #         node = self.storage[key]
    #         self.cache.move_to_end(node)
    #         return node
    #     else:
    #         return None
        

    # """
    # Adds the given key-value pair to the cache. The newly-
    # added pair should be considered the most-recently used
    # entry in the cache. If the cache is already at max capacity
    # before this entry is added, then the oldest entry in the
    # cache needs to be removed to make room. Additionally, in the
    # case that the key already exists in the cache, we simply
    # want to overwrite the old value associated with the key with
    # the newly-specified value.
    # """

    # def set(self, key, value):
    #     if key in self.storage:
    #         self.storage[key] = value
    #         # node = self.cache.find_value(key)
    #         self.cache.move_to_end(value)

    #     else:
    #         self.storage[key] = value
    #         self.cache.add_to_tail(value)  
    #         if self.size == self.limit:
    #             self.cache.remove_from_head()
    #             del self.storage[self.cache.head.value]
    #             self.size -= 1
    #     self.size += 1    


    # I haven't been able to get this code to pass tests at all today. I've tried and tried but I'm definitely missing something. I'm going to just push my code for now and take a break.        

    # # If the limit is at max - then remove the oldest value and reduce size by 1
    #     if self.size == self.limit:
    #         self.cache.remove_from_head()
    # # Remove from cache and also delete from storage?        
    #         # self.storage.head
    #         self.size -= 1
        

    # # If the key exists then overwrite and make it the most recent value
    #     if key in self.storage:
    #         #overwrite it
    #         self.storage.move_to_tail(key)
    #         return
    # # Otherwise, add the new key value pair to the tail of the cache and the dictionary
    #     self.cache.add_to_tail((key, value))
    #     print
    #     self.storage.tail = self.cache.tail
    #     self.size +=1        

# Solution code from US lecture:

# def get(self, key):
#     if key in self.storage:
#         node = self.storage[key]
#         self.order.move_to_end(node)
#         return node.value[1]

# def set(self, key, value):
#     if key in self.storage:
#         node = self.storage[key]
#         node.value = (key, value) 
#         self.order.move_to_end(node)
#         return
#     if self.size == self.limit:
#         del self.storage[self.order.head.value[0]]
#         self.order.remove_from_head()
#         self.size -= 1
#     self.order.add_to_tail((key, value))
#     self.storage[key] = self.order.tail
#     self.size += 1      
# 
# 
# Tom's solution:

def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.order = DoublyLinkedList
    self.storage = dict()

def get(self, key):
    # if the key exists in the storage
    if key in self.storage:
        # extract the node from storage at the key
        node = self.storage[key]
        # move the key to the end of the order
        self.order.move_to_end(node)
        # return the value of the value of the node
        return node.value[1]
    # otherwise
        # return None
    else:
        return None


def set(self, key, value):
    # if key exists in the storage
        # extract the node from the storage
        # set the node's value to the key value pair
        
        # call move to end on the order
        # return from the set method

    if key in self.storage:
        node = self.storage[key] 
        node.value = (key, value)
        self.order.move_to_end(node)
        return

    #if the size is the same as the limit
    if self.size == self.limit:
        # delete the storage at the head's value key
        del self.storage[self.order.head.value[0]]
        # call remove from head on the order
        self.order.remove_from_head()
        # decrement the size
        self.size -= 1
    #if both cases are false (does not run if top if statement is true)
    # call add to tail on the order passing in the key value pair
    self.order.add_to_tail((key, value))
    # set the storage at the index of the key to the order's tail
    self.storage[key] = self.order.tail
    # increment the size     
    self.size += 1


             
      
        

