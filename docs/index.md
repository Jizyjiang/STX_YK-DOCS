
# md网络视频测试

md网络视频测试

<video src="./source/video/X32_LoadScene.mp4" controls="controls" width="500" height="300">您的浏览器不支持播放该视频！</video>




<p align="center">
  <a href="https://squidfunk.github.io/mkdocs-material/">
    <img src="https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/.github/assets/logo.svg" width="320" alt="Material for MkDocs">
  </a>
</p>

<p align="center">
  <strong>
    A 
    <a href="https://material.io/">Material Design</a> 
    theme for 
    <a href="https://www.mkdocs.org/">MkDocs</a>
  </strong>
</p>


<head>
  <link href="https://vjs.zencdn.net/7.20.3/video-js.css" rel="stylesheet" />

  <!-- If you'd like to support IE8 (for Video.js versions prior to v7) -->
  <!-- <script src="https://vjs.zencdn.net/ie8/1.1.2/videojs-ie8.min.js"></script> -->
</head>

<body>
  <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
  <video
    id="my-video"
    class="video-js"
    controls
    preload="auto"
    width="640"
    height="264"
    poster="MY_VIDEO_POSTER.jpg"
    data-setup="{}"
  >
    <source src="./source/video/X32_LoadScene.mp4" type="video/mp4" />
  </video>
</body>