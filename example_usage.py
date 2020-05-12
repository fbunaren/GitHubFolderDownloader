from GitHubDownloader import Downloader

# Download All Files (*)

downloader = Downloader("https://github.com/fbunaren/imagecompression")
downloader.download("./example_result/all_files","*",True)

# Download __pycache__ folder
downloader = Downloader("https://github.com/fbunaren/imagecompression")
downloader.download("./example_result/pycache","__pycache__",True)