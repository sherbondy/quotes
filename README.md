This project relies on [PlotDevice](http://plotdevice.io/) to generate images.

The picture frames support 800x600 aspect ratio and mostly require JPEG photos:
```
mogrify -format jpg -quality 80% *.png
```

To batch convert the PNGs in the `img` folder.
