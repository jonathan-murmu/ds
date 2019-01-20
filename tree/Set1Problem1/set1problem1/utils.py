import collections


def display(tree):
    """Tree level order traversal"""
    if not tree:
        return
    nodes=collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes)!=0:
        currentNode=nodes.popleft()
        currentCount-=1
        if currentNode.main_member:
            main_member = currentNode.main_member.name
            main_member_gender = currentNode.main_member.gender
        else:
            main_member = main_member_gender = ''

        if currentNode.spouse:
            spouse = currentNode.spouse.name
            spouse_gender = currentNode.spouse.gender
        else:
            spouse = spouse_gender = ''

        print("{0}({1})-{2}({3})".format(main_member, main_member_gender, spouse, spouse_gender), end=', ' )
        nodes = nodes + collections.deque(currentNode.child_family)
        nextCount += len( currentNode.child_family)
        
        if currentCount==0:
            #finished printing current level
            print('\n')
            currentCount, nextCount = nextCount, currentCount