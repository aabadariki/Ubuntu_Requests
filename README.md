# An Image Fetcher

A Python script that fetches images from the web and downloads them to your local machine.

# Table of Contents

1. #introduction
2. #features
3. #requirements
4. #usage
5. #how-it-works
6. #troubleshooting

# Introduction

The Ubuntu Image Fetcher is a Python script that allows you to download images from the web and save them to your local machine. It's designed to be easy to use and efficient, with features like concurrent downloads and duplicate image detection.

# Features

- Fetches images from the web using URLs
- Saves images to a local directory
- Concurrent downloads for improved performance
- Duplicate image detection to avoid downloading the same image multiple times
- Error handling for connection issues and file saving errors

# Requirements

- Python 3.x
- requests library
- urllib library
- hashlib library
- concurrent.futures library

# Usage

1. Run the script using python Ubuntu_request.py
2. Enter the image URLs (separated by commas) when prompted
3. The script will download the images and save them to the Fetched_Images directory

# How it Works

1. The script prompts the user for image URLs
2. It uses the requests library to fetch the images from the web
3. It saves the images to the Fetched_Images directory using concurrent downloads
4. It detects duplicate images using MD5 hashes and skips them if they've already been downloaded

# Troubleshooting

- If you encounter connection issues, check your internet connection and try again
- If you encounter file saving errors, check the permissions on the Fetched_Images directory and try again
