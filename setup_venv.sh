#!/bin/bash

echo "Creating Python virtual environment..."
python3 -m venv venv

echo -e "\nActivating virtual environment..."
source venv/bin/activate

echo -e "\nInstalling dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

echo -e "\nVirtual environment setup complete!"
echo -e "\nTo activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo -e "\nTo deactivate the virtual environment, run:"
echo "  deactivate"
echo
