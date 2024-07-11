import streamlit as st

def main():
    st.title("Stack and Linting Functionality")

    st.header("Task 1: Explanation of Stack")
    st.write("""
        A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
        It allows operations such as push, pop, and peek.

        In a stack, elements are added and removed from the top, making it easy to track the most recent item. Here are the basic functionalities:
        - **Push:** Adds an element to the top of the stack.
        - **Pop:** Removes the top element from the stack.
        - **Peek/Read:** Returns the top element without removing it.
        - **IsEmpty:** Checks if the stack is empty.
    """)

    st.subheader("Time Complexities")
    st.write("""
        - **Push:**
            - Array/List Implementation: O(1) (on average, but resizing the array occasionally takes O(n) time)
            - Linked List Implementation: O(1)
        - **Pop:**
            - Array/List Implementation: O(1) (on average)
            - Linked List Implementation: O(1)
        - **Peek/Read:**
            - Array/List Implementation: O(1)
            - Linked List Implementation: O(1)

        **What does O(1) mean?**

        O(1) denotes constant time complexity. This means that the operation takes the same amount of time to complete, regardless of the size of the input data. For example, accessing an element in an array by its index, pushing or popping from a stack, and checking if a stack is empty are all O(1) operations. Whether you are processing 1 item or 1 million items, the time taken to perform the operation remains the same. O(1) operations are extremely efficient and predictable.
    """)

    st.header("Task 2: Stack as a Linter")
    st.write("""
        A stack can be used to check if the braces in a given string are balanced, which is a common linting task. Here’s how it works:

        Initialize a stack to hold opening braces. As you iterate through the string, push each opening brace onto the stack. For each closing brace, check if it matches the top of the stack. If it does, pop the top of the stack. If it doesn’t or if the stack is empty when you encounter a closing brace, the string is not balanced. Finally, if the stack is empty after processing all characters, the braces are balanced.
    """)

    st.code("""
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
    """, language='python')

    st.subheader("Scenarios")
    st.write("""
        **Scenario 1: No Mismatch**
        
        **Input:** `([]{})`
        
        - **Explanation:** As we process each character in the input:
            - Push `(` onto the stack: Stack becomes `[ ( ]`
            - Push `[` onto the stack: Stack becomes `[ ( [ ]`
            - Encounter `]`, it matches the top of the stack (`[`), so pop `[` from the stack: Stack becomes `[ ( ]`
            - Push `{` onto the stack: Stack becomes `[ ( { ]`
            - Encounter `}`, it matches the top of the stack (`{`), so pop `{` from the stack: Stack becomes `[ ( ]`
            - Encounter `)`, it matches the top of the stack (`(`), so pop `(` from the stack: Stack becomes `[]`
        - **Result:** The stack is empty at the end, indicating that all braces are balanced.

        **Scenario 2: Missing Closing Brace**
        
        **Input:** `((()`
        
        - **Explanation:** As we process each character in the input:
            - Push `(` onto the stack: Stack becomes `[ ( ]`
            - Push `(` onto the stack: Stack becomes `[ ( ( ]`
            - Push `(` onto the stack: Stack becomes `[ ( ( ( ]`
            - Encounter `)`, it matches the top of the stack (`(`), so pop `(` from the stack: Stack becomes `[ ( ( ]`
        - **Result:** The stack is not empty (`[ ( ( ]`), indicating that there are unmatched opening braces left, which means there are missing closing braces.

        **Scenario 3: Missing Opening Brace**
        
        **Input:** `())`
        
        - **Explanation:** As we process each character in the input:
            - Push `(` onto the stack: Stack becomes `[ ( ]`
            - Encounter `)`, it matches the top of the stack (`(`), so pop `(` from the stack: Stack becomes `[]`
            - Encounter `)`, the stack is empty, so there is no matching opening brace.
        - **Result:** The stack operation fails on the second `)`, indicating a missing opening brace.
    """)

if __name__ == "__main__":
    main()
