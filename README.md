

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-markdown">[![Contributor Covenant](https://img.shields.io/badge/code%20of%20conduct-Contributor%20Covenant-brightgreen.svg)](CODE_OF_CONDUCT.md)
</code></div></div></pre>

# Point Of Presence Python Client Library

A Python client library for interacting with a specific POP API. This library provides easy-to-use methods for performing GET, POST, PUT, PATCH and DELETE requests, with built-in authentication support.

## Table of Contents

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure you have Python 3.6 or higher installed. It's recommended to use a virtual environment.

### Option 1: Install from GitHub

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sci-ndp/pop-py.git
   cd pop-py
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install the package in editable mode:**

   ```bash
   pip install -e .
   ```
4. **Install development dependencies (optional, for testing):**

   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Install via pip

Once the package is published on PyPI, you can install it directly using pip:

```bash
pip install pointofpresence
```

## Running Tests

To run the tests, navigate to the project root and execute:

```bash
pytest
```

## Project Structure

> pop-py
> ├── pointofpresence/
> │   ├── init.py
> │   ├── base_client.py
> │   ├── get_method.py
> │   ├── post_method.py
> │   └── delete_method.py
> ├── tests/
> │   ├── init.py
> │   ├── test_base_client.py
> │   ├── test_get_method.py
> │   ├── test_post_method.py
> │   └── test_delete_method.py
> ├── .gitignore
> ├── LICENSE
> ├── README.md
> ├── requirements.txt
> └── setup.py

* **pointofpresence/** : Contains the source code of the library.
* **tests/** : Contains the test files for each module.
* **setup.py** : Configuration script for installing the library.
* **requirements.txt** : List of dependencies for development and testing.
* **README.md** : Project documentation.
* **LICENSE** : Project license.
* **.gitignore** : Specifies which files/directories Git should ignore.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/new-feature`)
3. **Make your changes** and **commit** (`git commit -m 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. **Open a Pull Reques**

Ensure your contributions follow the [contribution guidelines](CONTRIBUTING.md) if you have one.

## License

This project is licensed under the MIT License. See the [LICENSE]() file for details.
