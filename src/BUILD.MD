# Build instructions

1. Update set up file (change version)
2. Build package
```
python -m build  
```
3. Twine upload
```
twine upload dist/*   
```