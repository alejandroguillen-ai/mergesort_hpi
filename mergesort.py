from typing import List

def validate_input(l: List) -> bool:
    """
    Yashira Ramos
    Guarantees that the input list is a numeric type list (int | float)
    
    Args:
        l (List[int | float]): list to be checked
        
    Return:
        bool: whether the list is numeric (True) or not (False)
    """
    
    return None
    
def merge(l1: List[int | float], l2: List[int | float]) -> List[int | float]:
    """
    Alejandro Guillén
    Combines the elements of two sorted lists into a sorted list with those elements
    
    Args:
        l1 (List[int | float]): first sorted list.
        l2 (List[int | float]): second sorted list.
    
    Return:
        List[int | float]: sorted list with the elements of both l1 and l2
    """
    sorted_list = []
        
    i = j = 0
    s1, s2 = len(l1), len(l2)
        
    # Compare the smallest remaining element of each list
    while i < s1 and j < s2:
        if l1[i] <= l2[j]:
            sorted_list.append(l1[i])
            i += 1
        else:
            sorted_list.append(l2[j])
            j += 1            
                
    # One list is finished -> append the rest of the other one
    if i < s1: sorted_list += l1[i:]
    if j < s2: sorted_list += l2[j:]
        
    return sorted_list
    
    
def mergesort(main_list:List[int | float]) -> List[int | float]:
    """
    Javier Romero
    Divides the list into two halves that will be sorted
    
    Args:
        main_list (List[int | float]): non-sorted list
        
    Return:
        List[int | float]: list with the elements from main_list sorted
    """
    
    return None