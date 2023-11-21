class TreeNode:
    def _init_(self, key, name, phone):
        self.key = key
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None

class ContactManager:
    def _init_(self):
        self.root = None

    def insert(self, key, name, phone):
        self.root = self._insert_recursive(self.root, key, name, phone)

    def _insert_recursive(self, root, key, name, phone):
        if root is None:
            return TreeNode(key, name, phone)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key, name, phone)
        else:
            root.right = self._insert_recursive(root.right, key, name, phone)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"Name: {root.name}, Phone: {root.phone}")
            self.inorder_traversal(root.right)

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter contact key: "))
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact_manager.insert(key, name, phone)
            print("Contact added successfully!")

        elif choice == '2':
            key = int(input("Enter contact key to search: "))
            result = contact_manager.search(key)
            if result:
                print(f"Name: {result.name}, Phone: {result.phone}")
            else:
                print("Contact not found!")

        elif choice == '3':
            print("\nAll Contacts:")
            contact_manager.inorder_traversal(contact_manager.root)

        elif choice == '4':
            print("Exiting Contact Manager.")
            break

        else:
            print("Invalid choice. Please try again.")
main()
