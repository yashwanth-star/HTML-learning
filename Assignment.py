<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stack and Linting Functionality</title>
</head>
<body>
    <h1>Stack and Linting Functionality</h1>
    <h2>Task 1: Explanation of Stack</h2>
    <p>A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle. It allows operations such as push, pop, and peek.</p>
    <p>In a stack, elements are added and removed from the top, making it easy to track the most recent item. Here are the basic functionalities:</p>
    <ul>
        <li><strong>Push:</strong> Adds an element to the top of the stack.</li>
        <li><strong>Pop:</strong> Removes the top element from the stack.</li>
        <li><strong>Peek/Read:</strong> Returns the top element without removing it.</li>
        <li><strong>IsEmpty:</strong> Checks if the stack is empty.</li>
    </ul>
    <p><strong>Time Complexities:</strong></p>
    <ul>
        <li><strong>Push:</strong>
            <ul>
                <li>Array/List Implementation: O(1) (on average, but resizing the array occasionally takes O(n) time)</li>
                <li>Linked List Implementation: O(1)</li>
            </ul>
        </li>
        <li><strong>Pop:</strong>
            <ul>
                <li>Array/List Implementation: O(1) (on average)</li>
                <li>Linked List Implementation: O(1)</li>
            </ul>
        </li>
        <li><strong>Peek/Read:</strong>
            <ul>
                <li>Array/List Implementation: O(1)</li>
                <li>Linked List Implementation: O(1)</li>
            </ul>
        </li>
    </ul>
    <p>The differences in time complexities arise because arrays use contiguous memory, allowing direct access to elements, whereas linked lists use nodes that are dynamically allocated in memory, requiring traversal to access elements.</p>

    <h2>Task 2: Stack as a Linter</h2>
    <p>A stack can be used to check if the braces in a given string are balanced, which is a common linting task. Here’s how it works:</p>
    <p>Initialize a stack to hold opening braces. As you iterate through the string, push each opening brace onto the stack. For each closing brace, check if it matches the top of the stack. If it does, pop the top of the stack. If it doesn’t or if the stack is empty when you encounter a closing brace, the string is not balanced. Finally, if the stack is empty after processing all characters, the braces are balanced.</p>

    <p>Here’s a sample Python code to illustrate this:</p>
    <pre>
def is_balanced(input_string):
    stack = []
    opening_braces = {'(': ')', '{': '}', '[': ']'}
    closing_braces = {')': '(', '}': '{', ']': '['}

    for char in input_string:
        if char in opening_braces:
            stack.append(char)
        elif char in closing_braces:
            if not stack or stack[-1] != closing_braces[char]:
                return False
            stack.pop()

    return not stack

# Test cases
print(is_balanced("()"))          # True
print(is_balanced("([]{})"))      # True
print(is_balanced("({[)]}"))      # False
print(is_balanced("((()))"))      # True
print(is_balanced("((("))         # False
    </pre>

    <h3>Scenarios:</h3>
    <p><strong>No Mismatch:</strong> Input: <code>([]{})</code></p>
    <p>The stack after each step: <code>(</code>, <code>([</code>, <code>([]{</code>, <code>([]{}</code>, <code>([]{})</code>. Result: Balanced.</p>

    <p><strong>Missing Closing Brace:</strong> Input: <code>((()</code></p>
    <p>The stack after each step: <code>(</code>, <code>((</code>, <code>(((</code>, <code>((()</code>. Result: Not balanced, missing closing braces.</p>

    <p><strong>Missing Opening Brace:</strong> Input: <code>())</code></p>
    <p>The stack after each step: <code>(</code>, <code>()</code>, attempt to pop from an empty stack. Result: Not balanced, missing opening brace.</p>
</body>
</html>
