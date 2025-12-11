#Thomas Cubstead
#M7_Search_Trees_Project
#main
#12/10/25
#

from SearchTrees import BSTMap, AVLTreeMap
from schedule import Schedule
from schedule_item import ScheduleItem

# Test height of empty trees for both BST and AVL
def test_height_empty_tree():
    print("\n" + "=" * 80)
    print("Test: Height of Empty Trees")
    print("=" * 80)

    bst = BSTMap()
    avl = AVLTreeMap()

    bst_height = bst.height()
    avl_height = avl.height()

    print(f"BST empty height: {bst_height} (expected: -1)")
    print(f"AVL empty height: {avl_height} (expected: -1)")

    assert bst_height == -1, "BST empty tree should have height -1"
    assert avl_height == -1, "AVL empty tree should have height -1"

    print("Pass: Empty trees have correct height")

# Test height of trees with a single node for both BST and AVL
def test_height_single_node():
    print("\n" + "="*80)
    print("TEST: Height with Single Node")
    print("="*80)
    
    bst = BSTMap()
    avl = AVLTreeMap()
    
    bst.insert("key1", "value1")
    avl.insert("key1", "value1")
    
    bst_height = bst.height()
    avl_height = avl.height()
    
    print(f"BST single node height: {bst_height} (expected: 0)")
    print(f"AVL single node height: {avl_height} (expected: 0)")
    
    assert bst_height == 0, "BST single node should have height 0"
    assert avl_height == 0, "AVL single node should have height 0"
    
    print("Pass: Single node trees have correct height")

def test_height_balanced_insertion():
    print("\n" + "=" * 80)
    print("Test: Height with balanced insertion")
    print("="*80)

    bst = BSTMap()
    avl = AVLTreeMap()

    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values: