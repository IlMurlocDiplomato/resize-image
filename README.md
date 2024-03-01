# Resize-image


## Description

This script convert image and pdf to jpg format then resize it using image.thumbnail function.
The default value is 2000x2000.
The file size limit is incrase from 500Mb. It should be bigger but it may become a DOS attack, thats value its good for convert/resize big size image and limit potential vulnerability.

## Requirement

### Pillow 
```pip install Pillow ```
### Pdf2image
```pip install pdf2image ```

## Install

1. ```git clone https://github.com/IlMurlocDiplomato/resize-image.git```
2. ```python3 <directory, image, or list of image>```
3. ```The output file is genereted in a folder call output in the same directory of the script```
## Use

### Single file 
```python3 resize-image.py image.png ``` 
### By extension
```python3 resize-image.py img/*.png ```
### Full folder
```python3 resize-image.py img/ ```

# Thanks
Thanks to ImBiagio for the original script 
[ImBiagio](https://github.com/ImBiagio/resize-images)
