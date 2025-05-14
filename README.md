# Python Project 17.1

This project implements a simple product management system with categories and products.

## Features

- Product class with validation for zero quantity
- Category class with average price calculation
- Exception handling for invalid product creation
- Test coverage for all functionality

## Installation

1. Make sure you have Python 3.8+ installed
2. Install dependencies:
```bash
poetry install
```

## Running the Project

To run the main program:
```bash
python main.py
```

## Running Tests

To run tests with coverage:
```bash
poetry run pytest
```

## Project Structure

- `main.py` - Main program file
- `product.py` - Product class implementation
- `category.py` - Category class implementation
- `tests/` - Test files
  - `test_product.py` - Tests for Product class
  - `test_category.py` - Tests for Category class 