# -*- coding: utf-8 -*-
"""
Created on Wed Jul 30 13:50:23 2025

@author: hmoazami
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
        
    def insert(self, value):
        newNode = Node(value)
        
        if self.root == None:
            self.root = newNode
            return
        
        else:
            currentNode = self.root
            
            while True:
                #if newNode < currentNode.value: #newNode is object and CurrentNode is object as well. Python cant compare two node object they should be integer 
                if value < currentNode.value: #value is number given. we find value integer of currentNode by writin it as currentNode.value
                    #left
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return
                    else:
                        currentNode = currentNode.left
                        
                elif value >= currentNode.value:
                    #right
                    if currentNode.right ==None:
                        currentNode.right = newNode
                        return
                    else:
                        currentNode = currentNode.right
                        
    def lookup(self, value):
        if self.root == None:
            return False
        else:
            currentNode = self.root
            
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left 
            elif value > currentNode.value:
                currentNode = currentNode.right 
            elif value == currentNode.value:
                return currentNode  
        return False
 
    
    
    def remove(self, value):
        parentNode = None
        
        if self.root == None:
            return False
        else:
            currentNode = self.root
            
        while currentNode:
            
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left 
                
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right 
                
            elif value == currentNode.value:
                #if no right child
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left 
                    else: 
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        else: 
                            parentNode.right = currentNode.left
                            
                             
                # if has right child which doesn't have a left child
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                    else:
                        if parentNode.value < currentNode.value:
                            parentNode.right = currentNode.right
                        else: 
                            parentNode.left = currentNode.right
                            
                            
                #Option 3: Right child that has a left child
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left != None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                        
                    leftmostParent.left = leftmost.right
                    
                    leftmost.right = currentNode.right
                    leftmost.left = currentNode.left
                    
                    
                    if parentNode == None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                           parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                           parentNode.right = leftmost
                        
                    
                return True
                
                      
    def print_structure(self, node=None, prefix=""):
        if node is None:
            node = self.root
        if node.right:
            self.print_structure(node.right, prefix + "    ")
        print(prefix + "-> " + str(node.value))
        if node.left:
            self.print_structure(node.left, prefix + "    ")

        
    #def lookup():
        
tree = BinarySearchTree()
tree.insert(9) 
tree.insert(12) 
tree.insert(50)   
tree.insert(1) 
tree.insert(400) 
tree.insert(25) 

tree.remove(9) 

tree.print_structure()



def is_valid_BST(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.value < max_val):
        return False
    return (
        is_valid_BST(node.left, min_val, node.value) and
        is_valid_BST(node.right, node.value, max_val)
        )
print("Is valid BST?", is_valid_BST(tree.root))







        
        