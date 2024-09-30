class Node:
    """ 
    Clase que representa un nodo en una lista enlazada.
    
    Atributos:
        data: Contiene el valor almacenado en el nodo.
        next: Apunta al siguiente nodo en la lista enlazada, o None si es el último nodo.
    """

    def __init__(self, data):
        """
        Constructor de la clase Node.
        
        Args:
            data: El valor que almacenará el nodo.
        """
        self.data = data  # Almacena el valor del nodo
        self.next = None  # Inicialmente, el nodo no apunta a ningún otro nodo


class LinkedList:
    """ 
    Clase que representa una lista enlazada simple.

    Atributos:
        head: Apunta al primer nodo de la lista enlazada o None si la lista está vacía.
    """

    def __init__(self):
        """
        Constructor de la clase LinkedList.
        Inicializa la lista con la cabeza apuntando a None, indicando que la lista está vacía.
        """
        self.head = None  # La lista está vacía inicialmente

    def add_to_start(self, data):
        """
        Agrega un nuevo nodo al inicio de la lista enlazada.

        Args:
            data: El valor que se agregará al nuevo nodo.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor dado
        new_node.next = self.head  # El nuevo nodo apunta al nodo que antes era la cabeza
        self.head = new_node  # El nuevo nodo se convierte en la cabeza de la lista

    def add_to_end(self, data):
        """
        Agrega un nuevo nodo al final de la lista enlazada.

        Args:
            data: El valor que se agregará al nuevo nodo.
        """
        new_node = Node(data)  # Crea un nuevo nodo con el valor dado

        if self.head is None:
            self.head = new_node  # Si la lista está vacía, el nuevo nodo es la cabeza
            return

        last_node = self.head  # Empieza desde la cabeza
        while last_node.next:  # Recorre la lista hasta llegar al último nodo
            last_node = last_node.next

        last_node.next = new_node  # El último nodo apunta al nuevo nodo, que ahora es el último nodo

    def add_at_position(self, data, position):
        """
        Agrega un nuevo nodo en una posición específica de la lista enlazada.

        Args:
            data: El valor que se agregará al nuevo nodo.
            position: La posición en la que se insertará el nodo (0 para inicio).
        
        Raises:
            IndexError: Si la posición es negativa o fuera de los límites de la lista.
        """
        if position < 0:
            raise IndexError("La posición no puede ser negativa")

        new_node = Node(data)
        
        if position == 0:
            self.add_to_start(data)  # Si la posición es 0, agrega el nodo al inicio
            return

        current = self.head  # Comienza desde la cabeza
        index = 0
        
        while current and index < position - 1:  # Recorre la lista hasta la posición deseada
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Posición fuera de los límites")

        new_node.next = current.next  # Inserta el nuevo nodo en la posición especificada
        current.next = new_node

    def get_node_by_position(self, position):
        """
        Devuelve el valor de un nodo en una posición específica.

        Args:
            position: La posición del nodo a consultar.

        Returns:
            El valor almacenado en el nodo de la posición indicada.
        
        Raises:
            IndexError: Si la posición es negativa o está fuera de los límites de la lista.
        """
        if position < 0:
            raise IndexError("La posición no puede ser negativa")

        current = self.head  # Comienza desde la cabeza
        index = 0

        while current and index < position:  # Recorre la lista hasta llegar a la posición
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Posición fuera de los límites")

        return current.data  # Devuelve el valor en la posición dada

    def get_node_by_value(self, value):
        """
        Devuelve la posición de un nodo con un valor específico.

        Args:
            value: El valor del nodo a buscar.

        Returns:
            La posición del nodo con el valor indicado o -1 si no se encuentra.
        """
        current = self.head  # Comienza desde la cabeza
        position = 0

        while current:  # Recorre la lista
            if current.data == value:
                return position  # Devuelve la posición si encuentra el valor
            current = current.next
            position += 1

        return -1  # Devuelve -1 si no encuentra el valor

    def remove_by_value(self, value):
        """
        Elimina el primer nodo que contenga un valor específico.

        Args:
            value: El valor del nodo a eliminar.
        """
        current = self.head
        
        if current and current.data == value:  # Si el valor está en la cabeza
            self.head = current.next  # La cabeza apunta al siguiente nodo
            current = None  # Elimina el nodo
            return

        previous = None
        
        while current and current.data != value:  # Recorre la lista hasta encontrar el nodo con el valor
            previous = current
            current = current.next

        if current is None:
            return  # Si no encuentra el valor, no hace nada

        previous.next = current.next  # El nodo anterior apunta al siguiente nodo del actual
        current = None  # Elimina el nodo

    def remove_by_position(self, position):
        """
        Elimina un nodo en una posición específica.

        Args:
            position: La posición del nodo a eliminar.
        
        Raises:
            IndexError: Si la posición es negativa o está fuera de los límites de la lista.
        """
        if position < 0:
            raise IndexError("La posición no puede ser negativa")

        current = self.head

        if position == 0:  # Si la posición es 0, elimina la cabeza
            self.head = current.next
            current = None  # Elimina el nodo
            return

        previous = None
        index = 0
        
        while current and index < position:  # Recorre la lista hasta la posición deseada
            previous = current
            current = current.next
            index += 1

        if current is None:
            raise IndexError("Posición fuera de los límites")

        previous.next = current.next  # El nodo anterior apunta al siguiente nodo del actual
        current = None  # Elimina el nodo

    def display(self):
        """
        Muestra la lista enlazada desde la cabeza hasta el último nodo.
        """
        temp = self.head  # Comienza desde la cabeza
        while temp:  # Recorre la lista hasta que no haya más nodos
            print(temp.data, end=" -> ")  # Imprime el valor de cada nodo
            temp = temp.next
        print("None")  # Indica el final de la lista


# Ejemplo de Uso
# Crear una lista enlazada
ll = LinkedList()

# Agregar nodos
ll.add_to_start(10)  # Agrega 10 al inicio
ll.add_to_end(20)  # Agrega 20 al final
ll.add_at_position(15, 1)  # Agrega 15 en la posición 1 (entre 10 y 20)

# Mostrar la lista
ll.display()  # Salida esperada: 10 -> 15 -> 20 -> None

# Consultar nodos
print(ll.get_node_by_position(1))  # Salida esperada: 15
print(ll.get_node_by_value(20))  # Salida esperada: 2

# Eliminar nodos
ll.remove_by_value(15)  # Elimina el nodo con valor 15
ll.remove_by_position(1)  # Elimina el nodo en la posición 1 (que es ahora 20)

# Mostrar la lista después de eliminar
ll.display()  # Salida esperada: 10 -> None
