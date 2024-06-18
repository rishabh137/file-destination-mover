# file destination mover

Moves your files on its correct destination according to file extension at the time of downloading.

# The Problem
I wanted a solution that will automatically move the files to its correct file path at the time of downloading i.e. .mp3 in music folder, .mp4 in videos folder etc.

# The solution
I created this python program that will look into the downloads folder and if any change occurs in it then it will move the file to its correct folder as defined in program.





## Installation

The only way to get this program on your computer is by cloning this repo and by running:

```bash
git clone https://github.com/rishabh137/file-destination-mover.git
```


## Usage
Now you can customize it according to your directory and also can add more file extension according to you need.

```javascript
dir_music = "<your-destination-path>"
dir_video = "<your-destination-path>"
```

Run ``` python3 mover.py ``` and now you can download any file and it will move to its correct directory
