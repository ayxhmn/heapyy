![Heapyy Logo](logo.jpg)
<hr>

**heapyy** is a Python library for competitive programming, providing efficient implementations of common data structures and algorithms.

## 🚀 Features
- Singly Linked List
- Doubly Linked List
- (More coming soon!)

## 📦 Installation
```bash
pip install heapyy  # (If published on PyPI in the future)
```

Or install locally for development:

```bash
pip install -e .
```

## 🔥 Usage
Importing heapyy:

```python
import heapyy
```

Using singly linked list:

```python
from heapyy import LinkedList

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

print(ll.to_list())  # Output: [5, 10, 20, 30]

ll.remove(20)
print(ll.to_list())  # Output: [5, 10, 30]

print(ll.find(10))  # Output: True
print(ll.find(100))  # Output: False
```

## 🛠️ Development
Clone the repository:

```bash
git clone https://github.com/ayxhmn/heapyy.git
cd heapyy
```

Run tests:

```bash
python -m unittest discover tests
```

## 📜 License
MIT License

## 🤝 Contributing
Pull requests are welcome! If you want to add new algorithms or optimize existing ones, feel free to contribute.