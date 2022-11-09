# Video example
本地视频测试：
![type:video](./source/video/X32_LoadScene.mp4)


# 网络平台视频测试视频示例

Lorem ipsum dolor sit amet

![type:video-tag](./source/video/X32_LoadScene.mp4)




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
    <source src="MY_VIDEO.mp4" type="video/mp4" />
    <source src="MY_VIDEO.webm" type="video/webm" />
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank"
        >supports HTML5 video</a
      >
    </p>
  </video>

  <script src="https://vjs.zencdn.net/7.20.3/video.min.js"></script>
</body>