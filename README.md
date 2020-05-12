# GitHub Folder Downloader
- Created by Fransiscus Emmanuel Bunaren
- https://bunaren.com

`GitHubFolderDownloader` is a Python Library for downloading a folder in GitHub repository.

## Parameters
- `load_repository(url, branch)`
    - url : GitHub Repository URL (required)
    - branch : Chosen branch, the default value is "master" (optional)

- `download(destination,target_folder,recursive)`
    - destination : Folder path for storing all the downloaded files and directories (required)
    - target_folder : Selected directory in GitHub Repository, '*' is the default value (optional)

        Note : if target_folder is set to *, then all files and directories will be downloaded.

    - recursive : Download files and directories in subdirectories, the default value is True (optional)

## Usage
- Import the `GitHubDownloader.py` library to your Python code

    ```from GitHubDownloader import Downloader```

- Create an object of Downloader Class from GitHubDownloader
    
    ```
    downloader = Downloader(url,branch)
    ```

    Alternatively, you can leave the constructor parameter empty and call `load_repository` to load a repository.
    ```
    downloader = Downloader()
    downloader.load_repository(url,branch)
    ```
- Download Files by calling download method
    ```
    downloader.download(destination,target_folder,recursive)
    ```

## Example Use

Suppose that we have this Git Tree Structure
```
imagecompression
├───__pycache__
│   └───ImageCompression.cpython-38.pyc
├───ImageCompression.py
├───LICENSE
├───...
└───real-image.jpg
```
From GitHub Repository https://github.com/fbunaren/imagecompression


- For downloading all files and directories in the repository
    ```
    from GitHubDownloader import Downloader

    downloader = Downloader("https://github.com/fbunaren/imagecompression")
    downloader.download("./test","*",True)
    ```

- For downloading all files and directories in __ __pycache__ __ directory into `"./test"` folder

    ```
    from GitHubDownloader import Downloader

    downloader = Downloader("https://github.com/fbunaren/imagecompression")
    downloader.download("./test","__pycache__",True)
    ```
